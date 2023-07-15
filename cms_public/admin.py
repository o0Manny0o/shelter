from django.contrib import admin

from cms_public import models
from main.mixins import PublicTenantOnlyMixin


class SectionInline(admin.TabularInline):
    model = models.Section
    readonly_fields = ['slug']


@admin.register(models.Layout)
class LayoutAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    list_display = ('name',)
    inlines = [SectionInline]
