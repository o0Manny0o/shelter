from django.core.cache import cache

from settings.models import SiteConfiguration


class SiteConfigurationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.tenant.name != 'public':
            config = cache.get("site_config")
            if config is None:
                config = SiteConfiguration.get_solo()
                cache.set("site_config", config, None)
            request.config = config
        response = self.get_response(request)

        return response
