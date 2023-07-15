from django import forms

from cms.models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ["level"]