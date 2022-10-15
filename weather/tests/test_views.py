"""Test views."""
from django.urls import reverse
from rest_framework.test import APIClient

from weather.tests.test_models import ModelTests


class TestViews(ModelTests):

    """Test views requests or endpoints."""

    def setUp(self) -> None:
        """Setup configuration."""
        super(TestViews, self).setUp()
        self.client = APIClient()
        self.user = {
            "username": "user12",
            "email": "user@guiomentor.com",
            "password": "namungoona",
        }

        self.user_response = self.client.post(
            reverse("user:create"),
            self.user,
            format="json"
        )
        token = self.user_response.data.get("tokens", None).get("access", None)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {0}".format(token))

    def test_get_all_requests(self):
        """Get all requests"""
        request = self.client.get(reverse('weather-forecast'))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.json()['results']), 2)
