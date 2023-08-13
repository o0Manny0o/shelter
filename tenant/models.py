from django.db import models
from django.utils.safestring import mark_safe

from animals_public.models import DogBreed, CatBreed
from tenant import choices

ANIMALS = {
    "DOG": "Dog",
    "CAT": "Cat"
}


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=ANIMALS.items())


class Image(models.Model):
    title = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='images')
    order = models.IntegerField(unique=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='images')

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "100"/>')


class Dog(Animal):
    size = models.CharField(
        max_length=1,
        choices=choices.Sizes.choices,
        default=choices.Sizes.SMALL
    )

    breed = models.ForeignKey(DogBreed, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.type = ANIMALS["DOG"]
        super(Dog, self).save(*args, **kwargs)


class Cat(Animal):
    size = models.CharField(
        max_length=1,
        choices=choices.Sizes.choices,
        default=choices.Sizes.SMALL
    )

    breed = models.ForeignKey(CatBreed, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.type = ANIMALS["CAT"]
        super(Cat, self).save(*args, **kwargs)
