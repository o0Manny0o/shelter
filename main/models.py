from django.db import models
from django.dispatch import receiver
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.signals import post_schema_sync


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    auto_create_schema = True


class Domain(DomainMixin):
    pass


@receiver(post_schema_sync, sender=TenantMixin)
def created_user_client(sender, **kwargs):

    client = kwargs['tenant']
    print(client)