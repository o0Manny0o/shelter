from django.db import models
from django.dispatch import receiver
from django_tenants.models import TenantMixin
from django_tenants.signals import post_schema_sync
from django_tenants.utils import tenant_context
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    title = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='images')


@receiver(post_schema_sync, sender=TenantMixin)
def created_user_client(sender, **kwargs):
    client = kwargs['tenant']
    with tenant_context(client):
        SiteConfiguration.objects.create(title=client.name)
