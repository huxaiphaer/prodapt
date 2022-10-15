"""Test views."""
from django.urls import reverse

from weather.tests.test_models import ModelTests
from rest_framework.test import APIClient


class TestViews(ModelTests):

    """Test views requests or endpoints."""

    def setUp(self) -> None:
        """Setup configuration."""
        super(TestViews, self).setUp()
        self.client = APIClient()

    def test_get_all_requests(self):
        """Get all requests"""
        request = self.client.get(reverse('weather-forecast'))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.json()['results']), 2)
