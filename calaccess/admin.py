from django.contrib import admin
from calaccess import models

from calaccess.toolbox.autoregister import autoregister_admin

autoregister_admin(models)