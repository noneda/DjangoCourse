"""Serializer for the user API View."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User Object"""

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validate_data):
        """Create and return User with encrypted password"""
        return get_user_model().objects.create_user(**validate_data)
