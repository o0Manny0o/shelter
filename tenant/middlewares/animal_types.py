from tenant.models import Animal


class AnimalTypesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        animals = Animal.objects.values_list('type', flat=True).distinct()
        request.animals = animals
        response = self.get_response(request)

        return response
