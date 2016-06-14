from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import include, url
admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True,
    }),
)
