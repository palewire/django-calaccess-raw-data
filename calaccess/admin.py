from calaccess import models
from django.contrib import admin


class AbstractAdmin(admin.ModelAdmin):
    save_on_top = True


class CvrSoAdmin(AbstractAdmin):
    pass


admin.site.register(models.CvrSo, CvrSoAdmin)
