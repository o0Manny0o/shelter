from django.contrib import admin

from cms import models


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('level',)

