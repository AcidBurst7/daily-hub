import sqlite3
from backend.model.board import Board
from .init import conn, curs

curs.execute(
    """
    CREATE TABLE IF NOT EXISTS boards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """
)

def row_to_model(row: tuple) -> Board:
    (id, name) = row
    return Board(id=id, name=name)

def model_to_dict(board: Board) -> dict:
    return board.model_dump()

def get_one(id: int) -> Board:
    query = "SELECT * FROM boards WHERE id=:id"
    params = {"id": id}
    curs.execute(query, params)
    row = curs.fetchone()
    conn.commit()
    return row_to_model(row)

def get_all() -> list[Board]:
    query = "SELECT * FROM boards"
    curs.execute(query)
    conn.commit()
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(board: Board):
    query = """
        INSERT INTO boards (name) 
        VALUES (:name)
    """
    params = model_to_dict(board)
    curs.execute(query, params)
    conn.commit()
    return get_one(curs.lastrowid)

def modify(board: Board) -> Board:
    query = """
        UPDATE boards SET
            name = :name
        WHERE id = :id
    """
    params = model_to_dict(board)
    curs.execute(query, params)
    conn.commit()
    return get_one(board.id)

def delete(id: int) -> bool:
    query = """DELETE FROM boards WHERE id=:id"""
    params = {"id": id}
    result = curs.execute(query, params)
    conn.commit()
    return bool(result)