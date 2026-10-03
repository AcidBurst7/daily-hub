import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from ...models import Board, Column, Task, CheckList, CheckListItem


class Command(BaseCommand):
    help = "Создать демо-данные для пользователя"

    def add_arguments(self, parser):
        parser.add_argument(
            "--user-id",
            type=int,
            default=2,
            help="ID пользователя, для которого создаем доски, колонки и задачи",
        )

        parser.add_argument(
            "--clear",
            action="store_true",
            help="Удалить существующие демо-доски перед созданием",
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
                f"Пользователь с таким id={user_id} не существует"
            )

        data = self.load_demo_data()

        for board_data in data["boards"]:
            self.create_board(
                user=user,
                board_data=board_data,
                clear=clear,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Демо-данные успешно созданы."
            )
        )

    def load_demo_data(self):
        fixture_path = (
            Path(__file__).resolve().parents[2]
            / "fixtures"
            / "demo_data.json"
        )

        if not fixture_path.exists():
            raise CommandError(
                f"Файл с демо-данными не найден: {fixture_path}"
            )

        try:
            with fixture_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as exc:
            raise CommandError(
                f"Ошибка JSON в {fixture_path}: {exc}"
            )

    def create_board(self, user, board_data, clear):
        board_name = board_data["name"]

        if clear:
            Board.objects.filter(
                user=user,
                name=board_name,
            ).delete()

        board, board_created = Board.objects.get_or_create(
            user=user,
            name=board_name,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Доска: {board.name} "
                f"({'создана' if board_created else 'уже существует'})"
            )
        )

        columns = {}

        for column_data in board_data["columns"]:
            column, _ = Column.objects.get_or_create(
                board=board,
                name=column_data["name"],
                defaults={
                    "order": column_data["order"],
                },
            )

            columns[column_data["name"]] = column

            self.create_tasks(
                column=column,
                tasks_data=column_data.get("tasks", []),
            )

    def create_tasks(self, column, tasks_data):
        now = timezone.now()

        for data in tasks_data:
            defaults = {
                "description": data.get("description", ""),
                "order": data.get("order", 0),
                "color": data.get("color", "#ffffff"),
            }

            if "deadline_days" in data:
                defaults["deadline"] = (
                    now + timezone.timedelta(
                        days=data["deadline_days"]
                    )
                )

            if "completed_days_ago" in data:
                defaults["completed_at"] = (
                    now - timezone.timedelta(
                        days=data["completed_days_ago"]
                    )
                )

            task, _ = Task.objects.get_or_create(
                column=column,
                title=data["title"],
                defaults=defaults,
            )

            self.create_checklist(
                task=task,
                checklist_data=data.get("checklist"),
            )

    def create_checklist(self, task, checklist_data):
        if not checklist_data:
            return

        checklist, _ = CheckList.objects.get_or_create(
            task=task,
            name=checklist_data["name"],
        )

        for item_title in checklist_data.get("items", []):
            CheckListItem.objects.get_or_create(
                checklist=checklist,
                title=item_title,
            )
