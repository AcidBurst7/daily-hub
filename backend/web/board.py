from fastapi import APIRouter

from typing import Union

import backend.data.board as service
from backend.model.board import Board


router = APIRouter(prefix="/boards")

@router.get("/")
def get_all() -> list[Board]:
    return service.get_all()

@router.get("/{id}")
def get_one(id: int) -> Union[Board, None]:
    return service.get_one(id)

@router.post("/")
def create(board: Board) -> Board:
    return service.create(board)

@router.patch("/")
def modify(board: Board) -> Board:
    return service.modify(board)

@router.delete("/{id}")
def delete(board: Board) -> bool:
    return service.delete(board)