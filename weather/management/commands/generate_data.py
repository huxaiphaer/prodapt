"""Generate data for weather."""
import time
from datetime import datetime

from django.core.management import BaseCommand
import requests as req

from weather.constants import BASE_URL, WEATHER_API_KEY, CITIES_URL


class Command(BaseCommand):
    """Add weather data."""

    help = 'Populate weather data'

    def extract_cities(self):
        """
        Extract cities.

        :return Tuple of longitude and latitude.
        """
        try:
            cities_res = req.get(CITIES_URL)
            for i in cities_res.json():
                lat = i['coord']['lat']
                lon = i['coord']['lon']
                print(lat)
                print(lon)
                self.extract_weather_data(lat, lon)
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


        except Exception as e:
            raise Exception('Something went wrong with {error}'.format(error=e))

    def handle(self, *args, **kwargs):
        """Add weather data."""
        self.extract_cities()

