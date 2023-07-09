from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True


class DogBreed(Breed):
    class Meta(Breed.Meta):
        db_table = "dog_breeds"


class CatBreed(Breed):
    class Meta(Breed.Meta):
        db_table = "cat_breeds"
