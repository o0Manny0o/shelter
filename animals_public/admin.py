from django.contrib import admin

from animals_public import models


@admin.register(models.DogBreed)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.CatBreed)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name',)
