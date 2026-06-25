from fastapi import APIRouter

from typing import Union

import backend.service.task as service
from backend.model.task import Task


router = APIRouter(prefix="/tasks")

@router.get("/")
def get_all() -> list[Task]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> Union[Task, None]:
    return service.get_one(id)

@router.post("/")
def create(task: Task) -> Task:
    return service.create(task)

@router.patch("/")
def modify(task: Task) -> Task:
    return service.modify(task)

@router.delete("/{id}")
def delete(task: Task) -> bool:
    return service.delete(task)