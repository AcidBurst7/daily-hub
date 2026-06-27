from .init import (conn, curs)
from backend.model.board import Board
from backend.errors import Missing 

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
    return Board(
        id=id, 
        name=name
    )

def model_to_dict(board: Board) -> dict:
    return board.model_dump()

def get_one(id: int) -> Board:
    query = "SELECT * FROM boards WHERE id = ?"
    curs.execute(query, (id,))
    row = curs.fetchone()
    conn.commit()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Такой доски не существует")
    

def get_all() -> list[Board]:
    query = "SELECT * FROM boards"
    curs.execute(query)
    rows = list(curs.fetchall())
    conn.commit()
    return [row_to_model(row) for row in rows]


def create(board: Board) -> Board:
    query = """
        INSERT INTO boards (name) 
        VALUES (:name)
    """
    params = model_to_dict(board)
    curs.execute(query, params)
    conn.commit()
    return get_one(curs.lastrowid)

def modify(board: Board) -> Board:
    if not board: return None
    query = """
        UPDATE boards SET
            name = :name
        WHERE id = :id
    """
    params = model_to_dict(board)
    curs.execute(query, params)
    conn.commit()
    if curs.rowcount == 1:
        return get_one(board.id)
    else:
        raise Missing(msg=f"Такой доски не существует")

def delete(id: int):
    if not id: return False
    query = "DELETE FROM boards WHERE id = ?"
    curs.execute(query, (id,))
    conn.commit()
    if curs.rowcount != 1:
        return Missing(msg=f"Такой доски не существует.")
    else:
        return True