import uvicorn
from fastapi import FastAPI

from backend.web import (
    auth,
    task,
    board
)

app = FastAPI()
# app.include_router(weather_forecast.router)
app.include_router(auth.router)
app.include_router(board.router)
app.include_router(task.router)


if __name__ == "__main__":
    uvicorn.run("backend.src.main:app", reload=True)
