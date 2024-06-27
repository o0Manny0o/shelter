from django import forms

from cms.models import Page, PagePart


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ["level", 'layout', 'parent', 'name', 'slug', 'title', "icon"]

    def __init__(self, page, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        for part in page.parts.all():
            field_name = part.slug
            self.fields[field_name] = forms.CharField(required=True)
            self.initial[field_name] = part.content

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

    def save(self, **kwargs):
        page = self.instance
        print(page.name)
        for part in page.parts.all():
            print(self.cleaned_data[part.slug])
            part.content = self.cleaned_data[part.slug]
            part.save()


class PartForm(forms.ModelForm):
    class Meta:
        model = PagePart
        exclude = ["page", 'name', 'slug', 'title', "icon"]
