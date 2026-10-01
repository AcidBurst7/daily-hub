from django.core.mail import send_mail
from django.utils import timezone
from celery import shared_task

from .models import Task

@shared_task
def task_created(task_id: int):
    """
    Задание по отправке уведомления по электронной почте
    при успешном создании задачи
    """
    if task_id > 0:
        task = Task.objects.get(id=task_id)
        subject = f"📌У Вас новая задача."
        subject += f"Заголовок: {task.title}"

        message = f"""
            📜Описание задачи: {task.description}\n
            ⏰Дата и время создания: {task.created_at}\n
            ⏰Дата и время последнего изменения: {task.updated_at}\n
            ⏳ Срок выполнения задачи: {task.deadline}\n
        """

        print("TASK CREATED:")
        print(subject)
        print(message)

        mail_sent = send_mail(
            subject=subject, 
            message=message, 
            recipient_list=[task.column.board.user.email]
        )
        return {
            "status": True, 
            "msg": mail_sent
        }   

    return {
        "status": False, 
        "msg": "Номер сообщения не предоставлен"
    }