"""Test command for populating weather data."""
import datetime

from django.test import TestCase

from weather.management.commands.generate_data import Command


class ModelTests(TestCase):

    def setUp(self) -> None:
        """Setup tests config."""
        self.command = Command()

    def test_extract_by_city(self):
        """Extract data by a single city."""
        extract_data = self.command.extract_weather_data('52.5200', '13.4050')
        self.assertEqual(extract_data[0], 'Mitte')
        self.assertIsInstance(extract_data[1], str)
        self.assertIsInstance(extract_data[2], str)
        self.assertIsInstance(extract_data[3], datetime.datetime)
