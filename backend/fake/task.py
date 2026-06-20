from model.task import Task


_tasks = [
    Task(
        title="Простой питон",
        date_create="2026-06-20 15:03:00",
        task_text="Прочитать книгу 'Простой Python'",
        is_done=False,
        deadline_date="2026-07-20 23:59:59",
        board_id=1
    ),
    Task(
        title="Паттерны проектирования Python",
        date_create="2026-06-20 15:03:00",
        task_text="Прочитать книгу 'Паттерны проектирования Python'",
        is_done=False,
        deadline_date="2026-07-20 23:59:59",
        board_id=1
    ),
    Task(
        title="Алгоритмы Python",
        date_create="2026-06-20 15:03:00",
        task_text="Прочитать книгу 'Алгоритмы Python'",
        is_done=False,
        deadline_date="2026-07-20 23:59:59",
        board_id=1
    ),
    Task(
        title="Пет-проект",
        date_create="2026-06-20 15:03:00",
        task_text="1. сделать модели. 2. сделать заполнение фиктивными данными",
        is_done=False,
        deadline_date="2026-07-20 23:59:59",
        board_id=2
    ),
]

def get_all() -> list[Task]:
    """Возврат всех задач"""
    return _tasks

def get_one(title: str) -> Task:
    """Возврат конкретной задачи по заголовку"""
    for _task in _tasks:
        if _task.title == title:
            return _task
    return None

# Приведенные ниже варианты пока не функциональны,
# пока они просто длаю вид, что работают
# не изменяя реальный фиктивный список
def create(task: Task) -> Task:
    """Добавление задачи"""
    return task

def modify(task: Task) -> Task:
    """Частичное изменение задачи"""
    return task

def replace(task: Task) -> Task:
    """Полная замена записи задачи"""
    return task

def delete(task: Task) -> bool:
    """Удаление задачи или возврат пустоты, 
    если не существует записи"""
    return None
