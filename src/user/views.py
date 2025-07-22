"""
Views for user API.
Using a generic view that gives us DRF
"""

from rest_framework import generics
from user.serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user System"""

    serializer_class = UserSerializer
