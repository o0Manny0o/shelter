from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from main.mixins import PublicTenantOnlyMixin
from main.models import Client


@admin.register(Client)
class ClientAdmin(PublicTenantOnlyMixin, TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
