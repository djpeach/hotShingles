from django.contrib import admin
from . import models


@admin.register(models.Hottie)
class HottieAdmin(admin.ModelAdmin):
    pass
