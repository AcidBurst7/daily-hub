from backend.model.task import Task
from . import init
from backend.errors import Missing


def create_table():
    init.curs.execute("DROP TABLE IF EXISTS tasks")
    init.curs.execute(
        """
        CREATE TABLE tasks(
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
    init.conn.commit()

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
    init.curs.execute(query, (id, ))
    row = init.curs.fetchone()
    init.conn.commit()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Такой задачи не существует")

def get_all() -> list[Task]:
    query = "SELECT * FROM tasks"
    init.curs.execute(query)
    rows = list(init.curs.fetchall())
    init.conn.commit()
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
    init.curs.execute(query, params)
    init.conn.commit()
    return get_one(init.curs.lastrowid)

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
    init.curs.execute(query, params)
    init.conn.commit()
    if init.curs.rowcount == 1:
        return get_one(task.id)
    else:
        raise Missing(msg=f"Такой задачи не существует")

def delete(id: int):
    query = "DELETE FROM tasks WHERE id = ?"
    init.curs.execute(query, (id,))
    init.conn.commit()
    if init.curs.rowcount != 1:
        raise Missing(msg=f"Такой задачи не существует.")
    return True
    
