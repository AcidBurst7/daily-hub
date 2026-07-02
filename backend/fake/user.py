from backend.model.user import User
from errors import Duplicate, Missing

_users = [
    User(
        id=1,
        username="johndoe",
        first_name="John",
        last_name="Doe"
    )
]

def find(username: str) -> User|None:
    for _user in _users:
        if _user.username == username:
            return _user
    return None

def check_missing(username: str):
    if not find(username):
        raise Missing(msg=f"Пользователь с никнеймом {username} не найден.")

def get_all() -> list[User]:
    """Возврат всех пользователей"""
    return _users

def get_one(id: int) -> User:
    """Возврат конкретного пользователя"""
    for _user in _users:
        if _user.id == id:
            return _user
    return None
