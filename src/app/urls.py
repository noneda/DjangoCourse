from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include
from django.contrib import admin

"""
Get the following... To create documents with OPEN AI and Swagger, you need to create logical data... Where do you create this? In an APIView... and then, with Swagger, you get the information and create a view... I thought... maybe I'm wrong.
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="API Schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="API Schema"),
    ),
]
