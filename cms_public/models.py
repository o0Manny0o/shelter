import os

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def templates_path():
    return os.path.join(settings.BASE_DIR, "templates", "layouts")


class Layout(models.Model):
    name = models.CharField(max_length=50)
    template = models.FilePathField(path=templates_path, match=".html$")

    @classmethod
    def get_default_pk(cls):
        layout, created = cls.objects.get_or_create(
            name='default',
            template='default.html'
        )
        return layout.pk

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, related_name='sections')
    default = models.TextField()

    class Meta:
        unique_together = ('slug', 'layout')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)
