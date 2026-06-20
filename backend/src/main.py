import uvicorn
from fastapi import FastAPI

from backend.web import weather_forecast

app = FastAPI()
app.include_router(weather_forecast.router)

if __name__ == "__main__":
    uvicorn.run("backend.src.main:app", reload=True)
