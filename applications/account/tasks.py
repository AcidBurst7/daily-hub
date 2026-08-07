import time
from django.utils import timezone
from celery import shared_task


@shared_task
def update_last_seen():
    print(f"Beat works111! {timezone.now()}")
