print("!!! middleware.py imported !!!")

from django.core.cache import cache
from django.utils import timezone


class UserOnlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            key = f"user:{request.user.pk}:online"

            value = timezone.now().timestamp()

            cache.set(key, value, timeout=60)
        return self.get_response(request)