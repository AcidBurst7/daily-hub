import os
import pytest

from backend.model.task import Task
from backend.errors import Missing
from backend.service import task as service

os.environ["DAILYHUB_SQLITE_DB"] = ":memory:"
from data import task


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
    resp = service.create(sample)
    assert resp == sample
    
def test_get_one(sample):
    resp = service.get_one(sample.id)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = service.get_one(99999999)

def test_modify(sample):
    task.title = "Очень простой питон"
    resp = service.modify(sample.id, sample)
    assert resp == sample

def test_modify_missing(sample):
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
        _ = task.modify(thing.id, thing)

def test_delete(sample):
    resp = task.delete(sample.id)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = task.delete(sample.id)