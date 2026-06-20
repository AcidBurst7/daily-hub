from backend.model.task import Task
import backend.service.task as task_service


sample = Task(
    id=1,
    title="Простой питон",
    date_create="2026-06-20 15:03:00",
    task_text="Прочитать книгу 'Простой Python'",
    is_done=False,
    deadline_date="2026-07-20 23:59:59",
    board_id=1
)

def test_create():
    resp = task_service.test_create(sample)
    assert resp == sample

def test_get_exists():
    resp = task_service.get_one(sample.id)
    assert resp == sample

def test_get_missing():
    resp = task_service.get_one(111)
    assert resp is None