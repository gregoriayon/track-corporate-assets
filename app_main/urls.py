from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_main.swagger import urlpatterns as swagger_urls

from app_main.views import (
    index,
    CompanyViewSet,
    UserViewSet,
    EmployeeViewSet,
    DeviceViewSet,
    DeviceLogViewSet,
)

# Define Name
app_name = "app_main"

# Global API prefix variable
API_URL_PREFIX = "api"

router = DefaultRouter()

router.register(r'companies', CompanyViewSet)
router.register(r'users', UserViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = [
    path("home/", index, name="home" ),
    path(f"{API_URL_PREFIX}/", include(router.urls)),

    # Added swagger
    path("", include(swagger_urls)),
]