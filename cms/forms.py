from django import forms

from cms.models import Page, PagePart


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ["level", 'layout', 'parent', 'name', 'slug', 'title']

    def __init__(self, page, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        for part in page.parts.all():
            field_name = part.slug
            self.fields[field_name] = forms.CharField(required=True)
            self.initial[field_name] = part.content

    def clean(self):
        print(self.cleaned_data)

    # def save(self, **kwargs):
    #     page = self.instance
    #
    #     parts = page.parts.all()
    #     for part in parts:
    #         PagePart.objects.filter(slug=).update(
    #         )
