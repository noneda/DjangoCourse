"""
Test API for User
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# * Revere Function is for get a API for URL.name from the App
CREATE_USER_URL = reverse("user:create")


def createUser(**params):
    """Create and return a new User"""
    return get_user_model().objects.create_user(**params)


class PublicAPIUserTest(TestCase):
    """Test the public features of user API."""

    def setUp(self):
        """This make instance from Rest Framework to load a 'TEST' Endpoints... maybe... I'm really so bored of searching..."""
        self.client = APIClient()
        return super().setUp()

    def test_create_user_success(self):
        """Test creating user is Successful"""
        payload = {
            "email": "test@example.com",
            "password": "test_pass123",
            "name": "Test Name",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_with_email_exists_error(self):
        """Test error return when User with email exists"""
        payload = {
            "email": "test@example.com",
            "password": "test_pass123",
            "name": "Test Name",
        }
        createUser(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an Error is return if password less than 5 chars."""
        payload = {
            "email": "test@example.com",
            "password": "pw",
            "name": "Test Name",
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)
