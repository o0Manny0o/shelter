from django.core.cache import cache
from django_tenants.utils import tenant_context

from cms.models import Page


def find_parent(pages, slug):
    for page in pages:
        if page.slug == slug:
            return page
        if page.children:
            nested = find_parent(page.children, slug)
            if nested:
                return nested
    return None


def tenant_pages(request):
    if request.tenant.name == 'public':
        return {}
    pages = cache.get("tenant_pages")
    if pages is None:
        with tenant_context(request.tenant):
            pages = Page.objects.exclude(parent__isnull=False).select_related("parent")
            for page in pages:
                page.is_active(slug=request.path)
        cache.set("tenant_pages", list(pages), timeout=60)

    return {
        "pages": pages
    }
