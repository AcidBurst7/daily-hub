from fastapi import APIRouter

from typing import Union

import backend.fake.board as service
from backend.model.board import Board


router = APIRouter(prefix="/board")

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

@router.put("/")
def replace(board: Board) -> Board:
    return service.replace(board)

@router.delete("/{id}")
def delete(board: Board) -> bool:
    return service.delete(board)