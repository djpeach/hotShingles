from django.contrib import admin
from . import models


@admin.register(models.Shingle)
class ShingleAdmin(admin.ModelAdmin):
    pass
