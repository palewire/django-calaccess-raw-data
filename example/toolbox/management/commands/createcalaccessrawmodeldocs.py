import os
from django.conf import settings
from calaccess_raw import get_model_list
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Generate documentation for raw CAL-ACCESS database models'

    def handle(self, *args, **kwargs):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs'
        )
        self.target_path = os.path.join(self.docs_dir, 'models.rst')
        model_list = sorted(get_model_list(), key=lambda x:x().klass_name)
        group_list = {}
        empty_files = []
        for m in model_list:
            # add doc_id, page_url list to each model
            m.docs = {}
            for doc in m.DOCUMENTCLOUD_PAGES:
                doc_title = doc.get_doc_data()['title']
                try:
                    m.docs[doc_title].extend(
                        zip(
                            doc.get_page_urls(), doc.get_thumbnail_urls()
                        )
                    )
                except KeyError:
                    m.docs[doc_title] = list(zip(
                        doc.get_page_urls(), doc.get_thumbnail_urls()
                    ))
            # add choice field list to model
            m.choice_fields = []
            for field in m._meta.fields:
                if len(field.choices) > 0:
                    # add doc_id, page_url list to each choice field
                    field.docs = {}
                    for doc in field.documentcloud_pages:
                        doc_title = doc.get_doc_data()['title']
                        try:
                            field.docs[doc_title].extend(
                                zip(
                                    doc.get_page_urls(), doc.get_thumbnail_urls()
                                )
                            )
                        except KeyError:
                            field.docs[doc_title] = list(zip(
                                doc.get_page_urls(), doc.get_thumbnail_urls()
                            ))
                    m.choice_fields.append(field)
            try:
                group_list[m().klass_group].append(m)
            except KeyError:
                group_list[m().klass_group] = [m]
            if m.objects.count() == 0:
                empty_files.append(m)
        group_list = sorted(group_list.items(), key=lambda x:x[0])
        context = {
            'group_list': group_list,
            'model_count': len(model_list),
            'empty_files': empty_files,
        }
        rendered = render_to_string('toolbox/models.rst', context)
        with open(self.target_path, 'w') as target_file:
            target_file.write(rendered)
