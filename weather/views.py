"""Views for weather data."""
from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, response, status

from weather.constants import SEARCH_VALUE
from weather.models import WeatherForecast
from weather.serializers import WeatherForecastSerializer


class WeatherForecastView(generics.ListCreateAPIView):

    """WeatherForecastView class for rendering."""

    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def filter_queryset(self, queryset):
        """Filter the weather forecast."""
        ordering = self.request.GET.get("order_by", None)
        search = self.request.GET.get("search", None)

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

    def get(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        if not page:
            return response.Response({
                'errors': _('Sorry, no data for such a city.')
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
