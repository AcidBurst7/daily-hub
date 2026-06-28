import os
from pathlib import Path
import sqlite3

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
    
    conn = sqlite3.connect(name, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    return conn
