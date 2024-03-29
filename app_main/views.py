from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User

from app_main.models import (
    CompanyModel,
    EmployeeModel,
    DeviceModel,
    DeviceLogModel
)

from app_main.serializers import (
    UserSerializer,
    CompanySerializer,
    EmployeeSerializer,
    DeviceSerializer,
    DeviceLogSerializer
)

# Create your views here.

def index(request):
    return HttpResponse("Track Corporate Assets Project Home Page!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all().order_by('-id')
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all().order_by('-id')
    serializer_class = DeviceSerializer


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLogModel.objects.all().order_by('-id')
    serializer_class = DeviceLogSerializer
