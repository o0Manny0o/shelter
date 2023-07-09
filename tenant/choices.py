from django.db import models


class Sizes(models.TextChoices):
    SMALL = 'S', 'Small'
    MEDIUM = 'M', 'Medium'
    Large = 'L', 'Large'
