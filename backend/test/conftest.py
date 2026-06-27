import pytest
from pathlib import Path

from backend.data import init
from backend.data import task as task_data


@pytest.fixture(autouse=True)
def test_db():
    db = Path(__file__).parent / "test.db"

    # 💣 УДАЛЯЕМ БД ДО теста
    if db.exists():
        db.unlink()

    init.get_db(str(db), reset=True)
    task_data.create_table()
    init.conn.commit()

    yield

    init.conn.close()
    init.conn = None
    init.curs = None

    # 💣 УДАЛЯЕМ ПОСЛЕ теста
    if db.exists():
        db.unlink()