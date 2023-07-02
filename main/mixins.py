from django_tenants.utils import get_public_schema_name


class PublicTenantOnlyMixin:
    """Allow Access to Public Tenant Only."""

    def _only_public_tenant_access(self, request):
        return request.tenant.schema_name == get_public_schema_name()

    def has_view_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_add_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_change_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_delete_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_view_or_change_permission(self, request, view=None):
        return self._only_public_tenant_access(request)