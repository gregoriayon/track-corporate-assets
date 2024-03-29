from django.db import models
from django.contrib.auth.models import User


class CompanyModel(models.Model):
    name = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name


class EmployeeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    designation = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username


class DeviceModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name


class DeviceLogModel(models.Model):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition_on_check_out = models.CharField(max_length=100)
    condition_on_check_in = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.device.name} - {self.employee}"


