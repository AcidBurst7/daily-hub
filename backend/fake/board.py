from model.board import Board


_boards = [
    Board(name="Информация"),
    Board(name="Сделать"),
    Board(name="В процессе"),
    Board(name="Сделано"),
    Board(name="Архив"),
]

def get_all() -> list[Board]:
    """Возврат всех досок"""
    return _boards

def get_one(name: str) -> Board:
    """Возврат конкретной доски по имени"""
    for _board in _boards:
        if _board.name == name:
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

def delete(board: Board) -> bool:
    """Удаление записи или возврат пустоты, 
    если не существует записи"""
    return None
