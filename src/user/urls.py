"""
URL mapping for the user API.
"""

from django.urls import path
from user import views

# * M... this is a new...
app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
]
