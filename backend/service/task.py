from backend.model.task import Task
import backend.fake.task as data

def get_all() -> list[Task]:
    return data.get_all()

def get_one(id: int) -> Task | None:
    return data.get_one(id)

def create(board: Task) -> Task:
    return data.create(board)

def modify(board: Task) -> Task:
    return data.modify(board)

def replace(board: Task) -> Task:
    return data.replace(board)

def delete(id: int) -> bool:
    return data.delete(id)
