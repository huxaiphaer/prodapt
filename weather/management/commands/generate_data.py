"""Generate data for weather."""

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Add weather data."""

    help = 'Populate weather data'

    def handle(self, *args, **kwargs):
        """Add weather data."""
        print(" hey there ")
