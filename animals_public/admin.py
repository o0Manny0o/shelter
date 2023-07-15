from django.contrib import admin

from animals_public import models


@admin.register(models.DogBreed)
class DogBreedAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.CatBreed)
class CatBreedAdmin(admin.ModelAdmin):
    list_display = ('name',)
