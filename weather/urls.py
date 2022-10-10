"""weather app urls."""

from django.urls import path

from . import views

urlpatterns = [
    path('weatherforecast/',
         views.WeatherForecastView.as_view(), name='weather-forecast'),
]
