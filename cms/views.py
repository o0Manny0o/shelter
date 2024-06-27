from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.cache import cache_page

from cms.forms import PageForm
from cms.models import Page, PagePart
from shelterProject import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class PageView(View):
    @staticmethod
    def get(request, page_slug, *args, **kwargs):
        return PageView.render_page(request, page_slug, *args, **kwargs)

    @staticmethod
    def post(request, page_slug, *args, **kwargs):
        page = get_object_or_404(Page, slug=page_slug)
        page_form = PageForm(data=request.POST, page=page)
        if page_form.is_valid():
            print("valid")
            page_form.save()
        return PageView.render_page(request, page_slug, *args, **kwargs)

    @staticmethod
    def render_page(request, page_slug, *args, **kwargs):
        page = cache.get(page_slug)
        if page is None:
            page = Page.objects.select_related('layout').prefetch_related('layout__sections').get(
                slug=page_slug)
            cache.set(page_slug, page, CACHE_TTL)

        parts = cache.get(f"{page.slug}_parts")
        if parts is None:
            parts = page.parts.all()
            cache.set(f"{page.slug}_parts", list(parts))

        change = False
        for section in page.layout.sections.all():
            if next(filter(lambda part: part.slug == section.slug, parts), None) is None:
                PagePart.objects.create(page=page, slug=section.slug, content=section.default)
                change = True

        return render(
            request,
            page.layout.template,
            {
                'parts': {x.slug: x.content for x in (page.parts.all() if change else parts)},
                'is_edit': True,
                'page_form': PageForm(page=page),
                'page': page
            })
