from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True
