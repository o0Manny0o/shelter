from settings.models import SiteConfiguration


class SiteConfigurationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        config = SiteConfiguration.get_solo()
        request.config = config
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response