from django.shortcuts import get_object_or_404

from main.models import Client


class TenantDetailsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.user)
        client = get_object_or_404(Client, schema_name=request.tenant)
        print(client)
        request.tenant_name = client.name
        request.domain_url = client.domain_url

        response = self.get_response(request)

        return response
