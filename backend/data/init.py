import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str|None = None, reset: bool = False):
    """Подключение к файлу БД SQLite"""
    global conn, curs
    if conn:
        if reset:
            return
        conn = None
    if not name:
        name = os.getenv("DAILYHUN_SQLITE_DB")
        top_dir = Path(__file__).resolve().parents[1]
        db_dir = top_dir / "db"
        db_name = "dailyhub.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("DAILYHUB_SQLITE_DB", db_path)
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()

get_db()