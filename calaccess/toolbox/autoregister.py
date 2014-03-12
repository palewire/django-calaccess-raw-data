from types import ModuleType

from django.contrib import admin
from django.contrib.admin.util import quote
from django.contrib.admin.views.main import ChangeList
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db.models import ForeignKey, OneToOneField, Count
from django.db.models.base import ModelBase


def _get_admin_change_url(field):
    '''Return function to generate admin change view url for a related object.

    @param field: field pointing to a related object
    @type field: ForeignKey or OneToOneField
    '''

    related_model = field.related.parent_model

    def f(obj):
        link_args = getattr(obj, field.attname)
        if link_args is None:
            return u'(None)'
        # we could use field.name to output __unicode__() of the related object,
        # but that would require to prefetch related objects, which can be slow
        link_text = u'%s %s' % (related_model.__name__, getattr(obj, field.attname))

        try:
            url = reverse('admin:%s_%s_change' %
                            (related_model._meta.app_label, related_model._meta.module_name),
                          args=[quote(link_args)])
        except NoReverseMatch:
            return link_text
        return u'<a href="%s">%s</a>' % (url, link_text)
    f.allow_tags = True
    f.short_description = field.name
    return f


def _get_admin_changelist_url(source_field_name, target_model, target_field_name):
    '''Return function to generate admin changlelist view url for target_model.
    '''

    def f(obj):
        link_cond = '%s=%s' % (target_field_name, quote(obj.pk))
        link_text = u'%s (%s)' % (target_model._meta.verbose_name_plural.title(),
                                  getattr(obj, '%s__count' % source_field_name))

        try:
            url = reverse('admin:%s_%s_changelist' %
                            (target_model._meta.app_label, target_model._meta.module_name))
        except NoReverseMatch:
            return link_text
        return u'<a href="%s?%s">%s</a>' % (url, link_cond, link_text)
    f.allow_tags = True
    f.short_description = target_model.__name__
    return f


def _set_admin_queryset(admin_class, m2m_field_names, exclude_field_names):
    def queryset(self, request):
        qs = super(admin_class, self).queryset(request)
        if exclude_field_names:
            qs = qs.defer(*exclude_field_names)
        return qs
    admin_class.queryset = queryset

    # Now beware, the magic happens!
    # For each m2m relation, we would like to display the number of related
    # objects. To optimize it, we fetch the counts in one annotated query.
    # We could put this code in the above queryset() method, but...!
    # When Django admin asks for the total number of objects for pagination
    # purposes, it uses above-returned queryset for it. If we were to set
    # annotate (which performs multi-table joins) on that queryset, it would
    # result into VERY slow count() query.
    # That's why we are waiting with annotating until the last possible
    # moment, when the counts where already fetched.
    counts = [Count(c, distinct=True) for c in m2m_field_names]
    def get_changelist(self, *args, **kwargs):
        def get_results(self, request):
            super(self.__class__, self).get_results(request)
            if counts:
                self.result_list = self.result_list.annotate(*counts)
        return type('HackChangeList', (ChangeList,), {'get_results': get_results})
    admin_class.get_changelist = get_changelist


def _get_pk_func(field):
    def pk_func(obj):
        return getattr(obj, field.attname)
    pk_func.short_description = field.name
    return pk_func


def autoregister_admin(module, exclude_models=None, model_fields=None,
                       exclude_fields=None, admin_fields=None,
                       reversed_relations=None):
    '''
    @param module: module containing django.db.models classes
    @type module: str or __module__
                  If you are providing str, use absolute path.

    @param exclude_models: list of models to exclude from auto-register
    @type exclude_models: iterable of strings or None

    @param model_fields: dictionary of additional fields for list_display
        {model_name: [field_name1, field_name2, ...]}
    @type model_fields: dict or None

    @param exclude_fields: dictionary of fields to exclude from the models
        {model_name: [field_name1, field_name2, ...]}
    @type exclude_fields: dict or None

    @param admin_fields: dictionary of additional admin fields
        {model_name: {admin_field_name: value, ...}}
    @type admin_fields: dict or None

    @param reversed_relations: dictionary of additional reversed m2m/fk
                               relations to include to admin
        {model_name: [relation_name1, relation_name2, ...]}
    @type reversed_relations: dict or None
    '''

    exclude_models = set(exclude_models or [])
    model_fields = model_fields or {}
    exclude_fields = exclude_fields or {}
    admin_fields = admin_fields or {}
    reversed_relations = reversed_relations or {}
    if isinstance(module, basestring):
        module = __import__(module, fromlist=[module.split('.')[-1]])
    elif not isinstance(module, ModuleType):
        raise TypeError('invalid type of argument `module`, expected `str` or '
                        '`ModuleType`, got %s.' % type(module))

    # collect the models to register
    models = []
    for model in module.__dict__.values():
        if (isinstance(model, ModelBase) and
                model.__module__ == module.__name__ and
                not model._meta.abstract and
                model.__name__ not in exclude_models):
            models.append(model)

    # for each model prepare an admin class `<model_name>Admin`
    for model in models:
        model_name = model.__name__
        admin_class = type('%sAdmin' % model_name, (admin.ModelAdmin,), dict())
        admin_class.list_display = []
        admin_class.raw_id_fields = []
        exclude_field_names = set(exclude_fields.get(model_name, []))
        # add pk as the first value - access pk value through proxy, otherwise
        # when it is a related object, it is fetched too
        pk_field = model._meta.pk
        admin_class.list_display.append(_get_pk_func(pk_field))
        if isinstance(pk_field, (ForeignKey, OneToOneField)):
            admin_class.raw_id_fields.append(pk_field.name)
        # add other model fields
        for field in model._meta.fields:
            if field == model._meta.pk or field.name in exclude_field_names:
                continue
            if isinstance(field, (ForeignKey, OneToOneField)):
                admin_class.raw_id_fields.append(field.name)
                admin_class.list_display.append(_get_admin_change_url(field))
            else:
                admin_class.list_display.append(field.name)

        m2m_field_names = []
        # add m2m fields
        for field in model._meta.many_to_many:
            admin_class.raw_id_fields.append(field.name)
            m2m_field_names.append(field.name)
            change_list_url = _get_admin_changelist_url(
                field.name, field.related.parent_model, field.related_query_name())
            admin_class.list_display.append(change_list_url)

        # add reversed relations
        reversed_related_objs = (model._meta.get_all_related_objects() +
                                 model._meta.get_all_related_many_to_many_objects())
        allowed_reversed_relations = reversed_relations.get(model_name, [])
        for related in reversed_related_objs:
            related_name = related.field.related_query_name()
            if related_name not in allowed_reversed_relations:
                continue
            m2m_field_names.append(related_name)
            change_list_url = _get_admin_changelist_url(
                related_name, related.model, related.field.name)
            admin_class.list_display.append(change_list_url)

        # add custom model fields
        for name in model_fields.get(model_name, []):
            admin_class.list_display.append(name)

        # add custom admin fields
        for (name, value) in admin_fields.get(model_name, {}).iteritems():
            setattr(admin_class, name, value)

        _set_admin_queryset(admin_class, m2m_field_names, exclude_field_names)

        try:
            admin.site.register(model, admin_class)
        # pass gracefully on duplicate registration errors
        except admin.sites.AlreadyRegistered:
            pass
