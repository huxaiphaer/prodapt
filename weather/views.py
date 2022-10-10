"""Views for weather data."""
from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics

from weather.constants import SEARCH_VALUE
from weather.models import WeatherForecast
from weather.serializers import WeatherForecastSerializer


@method_decorator(cache_page(60 * 60), name='get')
@method_decorator(vary_on_cookie, name='get')
class WeatherForecastView(generics.ListCreateAPIView):

    """WeatherForecastView class for rendering."""

    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def filter_queryset(self, queryset):
        """Filter the weather forecast."""
        ordering = self.request.GET.get("order_by", None)
        search = self.request.GET.get("search", None)

        if search:
            queryset = queryset.annotate(
                rank=SearchRank(SearchVector('city'),
                                SearchQuery(search))).filter(
                rank__gte=SEARCH_VALUE)
        if search and ordering == 'asc':
            queryset = queryset.annotate(
                rank=SearchRank(SearchVector('city'),
                                SearchQuery(search))).filter(
                rank__gte=SEARCH_VALUE).order_by('date_time_forecasted')
        elif search and ordering == 'desc':
            queryset = queryset.annotate(
                rank=SearchRank(SearchVector('city'),
                                SearchQuery(search))).filter(
                rank__gte=SEARCH_VALUE).order_by('-date_time_forecasted')

        return queryset
