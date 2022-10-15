"""User tests."""
from django.test import TestCase
from django.urls import reverse


class UserTests(TestCase):

    """User tests"""
    def setUp(self) -> None:
        """Setup Tests."""
        self.user_data = {
            "username": "user12",
            "email": "user@guiomentor.com",
            "password": "namungoona",
        }

    def test_create_user(self):
        """Test create user."""
        self.user_response = self.client.post(
            reverse("user:create"),
            self.user_data,
            format="json"
        )
        self.assertEqual(self.user_response.status_code, 201)

    def test_login_user(self):
        """Test login user."""
        del self.user_data['username']
        self.user_response = self.client.post(
            reverse("user:login"),
            self.user_data,
            format="json"
        )
        self.assertEqual(self.user_response.status_code, 201)

    def test_failed_signup(self):
        """Test failed signup"""
        self.user_data['email'] = 'test'
        print(self.user_data)
        self.user_response = self.client.post(
            reverse("user:create"),
            self.user_data,
            format="json"
        )
        self.assertEqual(self.user_response.status_code, 400)

    def test_wrong_credentials(self):
        """Test wrong credentials login."""
        self.user_data['email'] = 'test@gmail.com'
        print(self.user_data)
        self.user_response = self.client.post(
            reverse("user:login"),
            self.user_data,
            format="json"
        )
        self.assertEqual(self.user_response.status_code, 400)
