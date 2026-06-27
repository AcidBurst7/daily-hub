from backend.model.task import Task
from .init import (conn, curs)
from backend.errors import Missing

curs.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date_create TEXT,
        task_text TEXT,
        is_done INTEGER,
        deadline_date TEXT,
        board_id INTEGER
    )
    """
)

def row_to_model(row: tuple) -> Task:
    return Task(
        id=row[0], 
        title=row[1], 
        date_create=row[2], 
        task_text=row[3], 
        is_done=row[4], 
        deadline_date=row[5], 
        board_id=row[6]
    )

def model_to_dict(board: Task) -> dict:
    return board.model_dump()

def get_one(id: int) -> Task:
    query = "SELECT * FROM tasks WHERE id = ?"
    curs.execute(query, (id, ))
    row = curs.fetchone()
    conn.commit()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Такой задачи не существует")

def get_all() -> list[Task]:
    query = "SELECT * FROM tasks"
    curs.execute(query)
    rows = list(curs.fetchall())
    conn.commit()
    return [row_to_model(row) for row in rows]

def create(task: Task) -> Task:
    query = """
        INSERT INTO tasks (
            title, date_create,
            task_text, is_done,
            deadline_date, board_id
        ) 
        VALUES (
            :title, :date_create,
            :task_text, :is_done,
            :deadline_date, :board_id
        )
    """
    params = model_to_dict(task)
    curs.execute(query, params)
    conn.commit()
    return get_one(curs.lastrowid)

def modify(task: Task) -> Task:
    if not task: None
    query = """
        UPDATE tasks SET
            title = :title, 
            date_create = :date_create,
            task_text = :task_text, 
            is_done = :is_done,
            deadline_date = :deadline_date, 
            board_id = :board_id
        WHERE id = :id
    """
    params = model_to_dict(task)
    curs.execute(query, params)
    conn.commit()
    if curs.rowcount == 1:
        return get_one(task.id)
    else:
        raise Missing(msg=f"Такой задачи не существует")

def delete(id: int):
    if not id: return False
    query = "DELETE FROM tasks WHERE id = ?"
    curs.execute(query, (id,))
    conn.commit()
    if curs.rowcount != 1:
        raise Missing(msg=f"Такой задачи не существует.")
    else:
        return True
