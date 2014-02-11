from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.static import serve as static_serve
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from django.views.generic import TemplateView
from campaign_finance import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^candidate/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.FilerView.as_view(template_name='filer/detail.html'), name='filer_detail'),
    url(r'^committees/(?P<pk>\d+)/$', views.CommitteeView.as_view(template_name='committee/detail.html'), name='committee_detail'),
    url(r'^search/', include('haystack.urls'), name='search'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r'^media/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )


if settings.PRODUCTION:
    urlpatterns += patterns('',
        url(r'^munin/(?P<path>.*)$', staff_member_required(static_serve), {
            'document_root': settings.MUNIN_ROOT,
        })
   )
