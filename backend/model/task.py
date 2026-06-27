from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    date_create: str
    task_text: str
    is_done: int
    deadline_date: str
    board_id: int
