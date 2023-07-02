from django.contrib import admin

from . import models


class ImagesInline(admin.TabularInline):
    model = models.Image
    ordering = ('order', )
    readonly_fields = ('img_preview', )


@admin.register(models.Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'size')
    inlines = [
        ImagesInline
    ]


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'size')
    inlines = [
        ImagesInline
    ]
