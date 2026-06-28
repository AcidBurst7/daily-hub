import pytest

from backend.model.board import Board
from backend.errors import Missing
from backend.data import board


@pytest.fixture
def sample() -> Board:
    return Board(id=1, name="Информация")

def test_create(sample):
    resp = board.create(sample)
    assert resp == sample
    
def test_get_one(sample):
    created = board.create(sample)
    resp = board.get_one(created.id)
    assert resp == created

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = board.get_one(99999999)

def test_modify(sample):
    created = board.create(sample)
    created.name = "Сделано"
    resp = board.modify(created)
    assert resp.name == "Сделано"

def test_modify_missing():
    thing: Board = Board(id=999, name="Архив")
    with pytest.raises(Missing):
        _ = board.modify(thing)

def test_delete(sample):
    created = board.create(sample)
    resp = board.delete(created.id)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = board.delete(sample.id)