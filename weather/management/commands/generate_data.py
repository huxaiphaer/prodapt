"""Generate data for weather."""
from datetime import datetime

import requests as req
from django.core.management import BaseCommand

from weather.constants import BASE_URL, CITIES_URL, WEATHER_API_KEY
from weather.models import WeatherForecast


class Command(BaseCommand):
    """Add weather data."""

    help = 'Populate weather data'

    def extract_all_data(self):
        """
        Extract cities and respective weather data.

        """
        try:
            cities_res = req.get(CITIES_URL)
            for i in cities_res.json():
                lat = i['coord']['lat']
                lon = i['coord']['lon']
                (city_name, description,
                 weather_type, date_time) = self.extract_weather_data(lat, lon)
                # Add weather data.
                WeatherForecast.objects.create(
                    city=city_name, description=description,
                    weather_type=weather_type, date_time_forecasted=date_time)
        except Exception as e:
            raise Exception('Something went wrong with {error}'.format(error=e))

    @staticmethod
    def extract_weather_data(latitude, longitude):
        """Extract weather data."""
        try:
            res = req.get(
                'https://{url}?lat={lat}&lon={lon}&appid={api_key}'.format(
                    url=BASE_URL, lat=latitude, lon=longitude,
                    api_key=WEATHER_API_KEY))

            city_name = res.json()['city']['name']

            for i in res.json()['list']:
                weather_type = i['weather'][0]['main']
                date_time = datetime.fromtimestamp(i['dt'])
                description = i['weather'][0]['description']

                return city_name, description, weather_type, date_time

        except Exception as e:
            raise Exception('Something went wrong with {error}'.format(error=e))

    def handle(self, *args, **kwargs):
        """Add weather data."""
        # Clear the tables first.
        WeatherForecast.objects.all().delete()

        self.extract_all_data()

        # TODO: Use logger instead of  print.
        print("---- DATA EXTRACTION DONE ----")
