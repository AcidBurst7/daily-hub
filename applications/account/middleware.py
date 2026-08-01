print("!!! middleware.py imported !!!")

from django.core.cache import cache
from django.utils import timezone


class UserOnlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            cache.set(
                f"user:{request.user.pk}:online",
                timezone.now().isoformat(),
                timeout=60
            )
        return self.get_response(request)