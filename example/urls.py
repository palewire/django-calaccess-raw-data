from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.views.static import serve
admin.autodiscover()


urlpatterns = (
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True,
    }),
)
