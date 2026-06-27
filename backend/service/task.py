from backend.model.task import Task
from backend.data import init
from backend.data import task as data

init.get_db()
data.create_tables()

def get_all() -> list[Task]:
    return data.get_all()

def get_one(id: int) -> Task | None:
    return data.get_one(id)

def create(task: Task) -> Task:
    return data.create(task)

def modify(task: Task) -> Task:
    return data.modify(task)

def delete(id: int):
    return data.delete(id)
