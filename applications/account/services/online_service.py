from datetime import datetime

from django.core.cache import cache
from django.utils import timezone


class OnlineService:
    @staticmethod
    def last_seen(user):
        value = cache.get(f"user:{user.pk}:online")
        if value is None:
            return None
        return datetime.fromtimestamp(float(value), tz=timezone.get_current_timezon())

    @staticmethod
    def is_online(user):
        return cache.get(f"user:{user.pk}:online") is not None