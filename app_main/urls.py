from django.urls import path
from app_main.views import *

app_name = "app_api"

# Global API prefix variable
API_URL_PREFIX = "api"

urlpatterns = [
    path("", index, name="api_home" ),
]