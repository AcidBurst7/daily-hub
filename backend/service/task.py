from backend.model.task import Task
import backend.data.task as data


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
