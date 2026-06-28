from fastapi import APIRouter, HTTPException
import backend.service.board as service
from backend.model.board import Board
from backend.errors import Missing


router = APIRouter(prefix="/boards", tags=["Доски"])


@router.get("/")
def get_all() -> list[Board]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> Board:
    try:
        return service.get_one(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=201)
def create(board: Board) -> Board:
    return service.create(board)

@router.patch("/")
def modify(board: Board) -> Board:
    try:
        return service.modify(board)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{id}")
def delete(id: int):
    try:
        return service.delete(id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)