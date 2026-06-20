from pydantic import BaseModel


class Forecast(BaseModel):
    weather_now: str
    temperature_now: str
    temperature_feel_now: str
    wind_value: str
    wind_direction: str
    wind_measure: str
    pressure_value: str
    pressure_measure: str
    wet_value: str
    wet_measure: str
    astro_title: str
    astro_sun_info: str
    astro_sun_about: str
    astro_moon_info: str
    astro_moon_about: str
