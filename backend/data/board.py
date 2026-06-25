import sqlite3
from model.board import Board


DB_NAME = "daily_nub_db.sql"
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()


def init():
    curs.execute("CREATE TABLE board(name)")

def row_to_model(row: tuple) -> Board:
    name = row
    return Board(name=name)

def model_to_dict(board: Board) -> dict:
    return board.dict()

def get_one(id: int) -> Board:
    query = "SELECT * FROM boards WHERE id=:id"
    params = {"id": id}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Board]:
    query = "SELECT * FROM boards"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(board: Board):
    query = """INSERT INTO boards (name) 
                VALUES (:name)"""
    params = model_to_dict(board)
    curs.execute(query, params)

def modify(board: Board):
    return board

def replace(board: Board):
    return board

def delete(id: int):
    query = """DELETE FROM boards WHERE id=:name"""
    params = {"id": id}
    curs.execute(query, params)
