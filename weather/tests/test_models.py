"""Unit test models."""
import datetime

from django.test import TestCase

from weather.models import WeatherForecast


class ModelTests(TestCase):

    """Model tests."""

    def setUp(self) -> None:
        """Model setup"""
        WeatherForecast.objects.create(
            city='Kampala', weather_type='sunny',
            description='Day is too bright',
            date_time_forecasted=datetime.date.today())
        WeatherForecast.objects.create(
            city='Kampala', weather_type='rainy',
            description='Day is too cold',
            date_time_forecasted=datetime.date.today())

    def test_weather_list_available(self):
        """Test if weather list available."""
        weather_items = WeatherForecast.objects.count()
        self.assertEqual(weather_items, 2)

    def test_empty_list_available(self):
        """Test empty list available."""
        WeatherForecast.objects.all().delete()
        weather_items = WeatherForecast.objects.count()
        self.assertEqual(weather_items, 0)

