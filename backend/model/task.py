from pydantic import BaseModel


class Task(BaseModel):
    title: str
    date_create: str
    task_text: str
    is_done: bool
    deadline_date: str

    board_id: int
