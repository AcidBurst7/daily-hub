from backend.model.board import Board
from backend.data import init
import backend.data.board as data


init.get_db()
data.create_table()


def get_all() -> list[Board]:
    return data.get_all()

def get_one(id: int) -> Board | None:
    return data.get_one(id)

def create(board: Board) -> Board:
    return data.create(board)

def modify(board: Board) -> Board:
    return data.modify(board)

def delete(id: int):
    return data.delete(id)
