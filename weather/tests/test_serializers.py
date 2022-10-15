"""Test serializers."""
import datetime

from django.test import TestCase

from weather.models import WeatherForecast
from weather.serializers import WeatherForecastSerializer


class TestSerializers(TestCase):
    """Test Serializers."""

    def setUp(self) -> None:
        self.data = {'city': 'Kampala',
                     'weather_type': 'sunny',
                     'description': 'Day is too bright',
                     'date_time_forecasted': datetime.date.today()}
        self.weather = WeatherForecast.objects.create(**self.data)
        self.serializer = WeatherForecastSerializer(
            self.weather, data=self.data)

    def test_valid_weather_forecast_serializer(self):
        """Test weather_forecast_serializer"""
        if self.serializer.is_valid():
            self.assertEqual(self.serializer.data, self.data)
