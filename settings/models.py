import environ
from django.db import models
from django.db.models import TextChoices
from django.dispatch import receiver
from django_tenants.models import TenantMixin
from django_tenants.signals import post_schema_sync
from django_tenants.utils import tenant_context
from solo.models import SingletonModel

env = environ.Env()


class LayoutChoices(TextChoices):
    SIDE_NAVIGATION = 'side_navigation.html',


class SiteConfiguration(SingletonModel):
    title = models.CharField(max_length=25, help_text="Page title displayed at the top of every page")
    logo = models.ImageField(upload_to='images/', default=env("DEFAULT_LOGO_URL"),
                             help_text="The logo next to the title")
    hero = models.ImageField(upload_to='images/', null=True, blank=True)
    base_layout = models.CharField(choices=LayoutChoices.choices, default=LayoutChoices.SIDE_NAVIGATION)

    def __str__(self):
        return "Site Configuration"

    def get_layout(self):
        return "layouts/" + LayoutChoices(self.base_layout)


@receiver(post_schema_sync, sender=TenantMixin)
def created_user_client(sender, **kwargs):
    client = kwargs['tenant']
    if client.name != 'public':
        with tenant_context(client):
            SiteConfiguration.objects.create(title=client.name)
