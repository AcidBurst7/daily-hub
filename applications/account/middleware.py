from config.redis import redis_client
from django.utils import timezone


class UserOnlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            key = f"user:{request.user.pk}:online"

            if redis_client.ttl(key) < 30:
                redis_client.set(
                    key, 
                    timezone.now().timestamp(),
                    ex=60
                )
        return self.get_response(request)