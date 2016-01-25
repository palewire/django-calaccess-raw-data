#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True

    def get_readonly_fields(self, *args, **kwargs):
        return [f.name for f in self.model._meta.fields]
