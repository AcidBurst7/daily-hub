import os
from pathlib import Path
from sqlite3 import connect, Row, IntegrityError

conn = None
curs = None

def get_db(name: str | None = None, reset: bool = False):
    """Подключение к файлу БД SQLite"""
    global conn, curs

    if conn is not None:
        if not reset:
            return conn
        conn.close()

    if name is None:
        top_dir = Path(__file__).resolve().parents[1]
        db_dir = top_dir / "db"
        db_name = "dailyhub.db"
        name = os.getenv("DAILYHUB_SQLITE_DB", str(db_dir / db_name))
    
    conn = connect(name, check_same_thread=False)
    conn.row_factory = Row
    curs = conn.cursor()

    return conn
