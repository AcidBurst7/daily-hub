import pytest

from backend.model.task import Task
from backend.errors import Missing
from backend.data import task


@pytest.fixture
def sample() -> Task:
    return Task(
        id=1,
        title="Простой питон",
        date_create="2026-06-20 15:03:00",
        task_text="Прочитать книгу 'Простой Python'",
        is_done=False,
        deadline_date="2026-07-20 23:59:59",
        board_id=1
    )

def test_create(sample):
    resp = task.create(sample)
    assert resp == sample
    
def test_get_one(sample):
    created = task.create(sample)
    resp = task.get_one(created.id)
    assert resp == created

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = task.get_one(99999999)

def test_modify(sample):
    created = task.create(sample)
    created.title = "Очень простой питон"
    resp = task.modify(created)
    assert resp.title == "Очень простой питон"

def test_modify_missing():
    thing: Task = Task(
                id=999,
                title="Тестовая задача",
                date_create="2026-06-20 15:03:00",
                task_text="что-то сделать",
                is_done=True,
                deadline_date="2026-07-20 23:59:59",
                board_id=1
            )
    with pytest.raises(Missing):
        _ = task.modify(thing)

def test_delete(sample):
    created = task.create(sample)
    resp = task.delete(created.id)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = task.delete(sample.id)