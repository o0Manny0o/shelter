from django.db import models
from cms_public.models import Layout


class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50, null=False, blank=False, default='My new page')
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, blank=True, related_name='children')
    level = models.IntegerField(default=0)
    layout = models.ForeignKey(Layout, on_delete=models.SET_DEFAULT, default=Layout.get_default_pk, related_name='pages')
    icon = models.CharField(blank=True, null=True)
    active = False


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
        if self._state.adding:
            for section in self.layout.sections.all():
                PagePart.objects.get_or_create(page=self, slug=section.slug, content=section.default)

    def is_active(self, slug):
        if self.slug in [x for x in slug.split("/") if x]:
            self.active = True
            return True
        else:
            for child in self.children.all():
                if child.is_active(slug=slug):
                    self.active = True
                    return True
        return False

    def __str__(self):
        return self.name


class PagePart(models.Model):
    slug = models.SlugField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='parts')
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.slug
