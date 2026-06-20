from fastapi import APIRouter

from backend.service.parsers.gismeteo import WeatherForecast


router = APIRouter(prefix="/weather_forecast")

@router.get("/{city}")
def get_forecast(city: str):
    weather_forecast = WeatherForecast(city)
    return weather_forecast.process()