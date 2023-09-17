from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cms.forms import PageForm
from cms.models import Page, PagePart


class PageView(View):
    @staticmethod
    def get(request, page_slug, *args, **kwargs):
        page = get_object_or_404(Page, slug=page_slug)
        parts = page.parts.all()
        sections = page.layout.sections.all()
        for section in sections:
            if next(filter(lambda part: part.slug == section.slug, parts), None) is None:
                PagePart.objects.create(page=page, slug=section.slug, content=section.default)
        return render(
            request,
            page.layout.template,
            {
                'parts': {x.slug: x.content for x in page.parts.all()},
                'is_edit': True,
                'page_form': PageForm(page=page),
                'page': page
            })

    @staticmethod
    def post(request, page_slug, *args, **kwargs):
        page = get_object_or_404(Page, slug=page_slug)
        page_form = PageForm(data=request.POST, page=page)
        if page_form.is_valid():
            print("valid")
        return redirect('tenant:welcome')
