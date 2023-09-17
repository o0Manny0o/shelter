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
    with tenant_context(request.tenant):
        pages = Page.objects.prefetch_related('children').exclude(parent__isnull=False)
        for page in pages:
            page.is_active(slug=request.path)

    return {
        "pages": pages
    }
