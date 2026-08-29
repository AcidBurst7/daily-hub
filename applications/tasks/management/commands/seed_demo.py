from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone


from applications.tasks.models import Board, Column, Task, CheckList, CheckListItem


class Command(BaseCommand):
    help = "Создать демо-данные для пользователя"

    def add_arguments(self, parser):
        parser.add_argument(
            "--user-id",
            type=int,
            default=2,
            help="ID для пользователя для которого создаем доски, колонки, задачи"
        )

        parser.add_argument(
            "--clear",
            action="store_true",
            help="Удалить существующую доску перед удалением"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        user_id = options["user_id"]
        clear = options["clear"]

        User = get_user_model()

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise CommandError(
                f"Пользоатель с таким id={user_id} не существует" 
            )

        boards_names = ["Мой проект"]

        for board_name in boards_names:
            if clear:
                Board.objects.filter(
                    user=user,
                    name=board_name
                ).delete()

            board, board_created = Board.objects.get_or_create(
                user=user,
                name=board_name,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Доска: {board.name}"
                    f"({'создана' if board_created else 'уже существует'})"
                )
            )

        columns_data = [
            {
                "name": "Идеи",
                "order": 1,
            },
            {
                "name": "К выполнению",
                "order": 2,
            },
            {
                "name": "В работе",
                "order": 3,
            },
            {
                "name": "На проверке",
                "order": 4,
            },
            {
                "name": "Готово",
                "order": 5,
            },
        ]

        columns = {}

        for data in columns_data:
            column, _ = Column.objects.get_or_create(
                board=board,
                name=data["name"],
                defaults={
                    "order": data["order"],
                },
            )

            columns[data["name"]] = column

        now = timezone.now()

        tasks_data = [
            {
                "column": "Идеи",
                "title": "Добавить тёмную тему",
                "description": "Продумать цветовую схему и переключатель темы.",
                "order": 0,
                "color": "#ffffff",
            },
            {
                "column": "Идеи",
                "title": "Добавить поиск по задачам",
                "description": "Поиск по названию и описанию задачи.",
                "order": 1,
                "color": "#0d6efd",
            },
            {
                "column": "К выполнению",
                "title": "Настроить страницу профиля",
                "description": "Имя пользователя, email и изменение пароля.",
                "order": 0,
                "color": "#198754",
            },
            {
                "column": "К выполнению",
                "title": "Добавить фильтрацию задач",
                "description": "Фильтр по колонке, цвету и статусу.",
                "order": 1,
                "color": "#ffc107",
                "deadline": now + timezone.timedelta(days=7),
            },
            {
                "column": "В работе",
                "title": "Реализовать drag-and-drop",
                "description": "Перемещение задач между колонками и изменение порядка.",
                "order": 0,
                "color": "#dc3545",
            },
            {
                "column": "В работе",
                "title": "Написать тесты для Task API",
                "description": "Проверить создание, изменение и удаление задач.",
                "order": 1,
                "color": "#6f42c1",
            },
            {
                "column": "На проверке",
                "title": "Проверить авторизацию",
                "description": "Проверить доступ пользователя к собственным доскам.",
                "order": 0,
                "color": "#EC4899",
            },
            {
                "column": "Готово",
                "title": "Настроить CI/CD",
                "description": "Запуск тестов и деплой после push в main.",
                "order": 0,
                "color": "#fd7e14",
                "completed_at": now,
            },
        ]

        for data in tasks_data:
            column = columns[data["column"]]

            defaults = {
                "description": data["description"],
                "order": data["order"],
                "color": data["color"],
            }

            if "deadline" in data:
                defaults["deadline"] = data["deadline"]

            if "completed_at" in data:
                defaults["completed_at"] = data["completed_at"]

            task, _ = Task.objects.get_or_create(
                column=column,
                title=data["title"],
                defaults=defaults,
            )

            if task.title == "Настроить CI/CD":
                checklist, _ = CheckList.objects.get_or_create(
                    task=task,
                    name="Что проверить",
                )

                checklist_items = [
                    "Проверить GitHub Actions",
                    "Проверить запуск тестов",
                    "Проверить переменные окружения",
                    "Проверить deploy",
                ]

                for item_title in checklist_items:
                    CheckListItem.objects.get_or_create(
                        checklist=checklist,
                        title=item_title,
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Демо-данные успешно созданы."
            )
        )

