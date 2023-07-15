from django.db import models

from cms_public.models import Layout


class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, blank=True, related_name='children')
    level = models.IntegerField(default=0)
    layout = models.ForeignKey(Layout, on_delete=models.SET_DEFAULT, default=Layout.get_default_pk, related_name='pages')

    title = models.CharField(max_length=50, null=False, blank=False, default='Title')

    def save(self, *args, **kwargs):
        if self.parent:
            try:
                parent = Page.objects.get(id=self.parent.id)
                if self == parent:
                    self.parent = None
                    self.level = 0
                else:
                    self.level = self.parent.level + 1
            except Page.DoesNotExist:
                pass
        super(Page, self).save(*args, **kwargs)
        for section in self.layout.sections.all():
            PagePart.objects.get_or_create(page=self, slug=section.slug, content=section.default)

    def __str__(self):
        return self.name


class PagePart(models.Model):
    slug = models.SlugField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='parts')
    content = models.TextField(max_length=2000)
