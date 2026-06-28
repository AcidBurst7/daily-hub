import os
import sys
import pytest
from pathlib import Path

from backend.data import init
from backend.data import task as task_data


@pytest.fixture(autouse=True)
def test_db():
    top_dir = Path(__file__).resolve().parents[1]
    db_dir = top_dir / "db"
    db = db_dir / "test.db"
    
    if db.exists():
        db.unlink()

    init.get_db(str(db), reset=True)
    task_data.create_table()
    init.conn.commit()

    yield

    init.conn.close()
    init.conn = None
    init.curs = None

    if db.exists():
        db.unlink()