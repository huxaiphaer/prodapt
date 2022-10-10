"""Weather filters"""

from django_filters import rest_framework as filters

from weather.models import WeatherForecast


class WeatherFilter(filters.FilterSet):

    """Weather filter set."""

    class Meta:
        model = WeatherForecast
        fields = ('city',)
