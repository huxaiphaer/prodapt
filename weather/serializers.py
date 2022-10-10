"""Serializers."""
from rest_framework import serializers

from weather.models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):

    """WeatherForecast Serializer."""

    class Meta:
        """Class Meta for WeatherForecastSerializer. """
        model = WeatherForecast
        fields = (
            'uuid', 'city', 'weather_type',
            'description', 'date_time_forecasted',)
