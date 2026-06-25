from backend.model.board import Board
import backend.data.board as data

def get_all() -> list[Board]:
    return data.get_all()

def get_one(id: int) -> Board | None:
    return data.get_one(id)

def create(board: Board) -> Board:
    return data.create(board)

def modify(board: Board) -> Board:
    return data.modify(board)

def delete(id: int) -> bool:
    return data.delete(id)
