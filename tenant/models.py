from cloudinary import CloudinaryImage
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

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='images/')
    order = models.IntegerField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='images')

    class Meta:
        unique_together = ('order', 'animal')

    def img_preview(self):  # new
        return mark_safe(CloudinaryImage(self.image.name).image(transformation=['pet_100'], sign_url=True))


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
