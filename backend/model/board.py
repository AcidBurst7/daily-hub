from pydantic import BaseModel


class Board(BaseModel):
    id: int
    name: str