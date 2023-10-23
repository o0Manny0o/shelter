from settings.models import SiteConfiguration


class SiteConfigurationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.tenant.name != 'public':
            config = SiteConfiguration.get_solo()
            request.config = config
            request.base_layout = config.get_layout()
        response = self.get_response(request)

        return response
