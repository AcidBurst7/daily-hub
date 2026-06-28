from fastapi import APIRouter, HTTPException
import backend.service.task as service
from backend.model.task import Task
from backend.errors import Missing


router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/")
def get_all() -> list[Task]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> Task:
    try:
        return service.get_one(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=201)
def create(task: Task) -> Task:
    return service.create(task)

@router.patch("/")
def modify(task: Task) -> Task:
    try:
        return service.modify(task)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{id}", status_code=204)
def delete(id: int):
    try:
        return service.delete(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)