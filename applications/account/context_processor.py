from django.core.cache import cache
from django.utils import timezone


def online_status(request):
    if not request.user.is_authenticated:
        return {}

    key = f"user:{request.user.pk}:online"

    last_seen = cache.get(key)

    return {
        "is_online": True,
        "last_seen": last_seen if last_seen else None
    }