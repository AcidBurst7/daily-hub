from backend.model.board import Board


_boards = [
    Board(id=1, name="Информация"),
    Board(id=2, name="Сделать"),
    Board(id=3, name="В процессе"),
    Board(id=4, name="Сделано"),
    Board(id=5, name="Архив"),
]

def get_all() -> list[Board]:
    """Возврат всех досок"""
    return _boards

def get_one(id: int) -> Board:
    """Возврат конкретной доски по имени"""
    for _board in _boards:
        if _board.id == id:
            return _board
    return None

# Приведенные ниже варианты пока не функциональны,
# пока они просто длаю вид, что работают
# не изменяя реальный фиктивный список
def create(board: Board) -> Board:
    """Добавление доски"""
    return board

def modify(board: Board) -> Board:
    """Частичное изменение доски"""
    return board

def replace(board: Board) -> Board:
    """Полная замена записи доски"""
    return board

def delete(id: int) -> bool:
    """Удаление записи или возврат пустоты, 
    если не существует записи"""
    return True
