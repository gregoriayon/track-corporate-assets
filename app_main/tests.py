from django.test import TestCase
from django.contrib.auth.models import User
from .models import CompanyModel, EmployeeModel, DeviceModel, DeviceLogModel
from datetime import datetime, timedelta
from django.utils import timezone


class ModelsTestCase(TestCase):
    def setUp(self):
        self.company = CompanyModel.objects.create(name='Example Company')


        self.user = User.objects.create_user(
            username='john_doe', password='testpassword', first_name='John', last_name='Doe'
        )


        self.employee = EmployeeModel.objects.create(
            user=self.user, company=self.company, phone='1234567890', designation='Developer'
        )


        self.device = DeviceModel.objects.create(name='Test Device', description='Test Description')


        self.check_out_date = timezone.now()
        self.device_log = DeviceLogModel.objects.create(
            device=self.device,
            employee=self.employee,
            check_out_date=self.check_out_date,
            condition_on_check_out='Good'
        )

    def test_company_model(self):
        company = CompanyModel.objects.get(name='Example Company')
        self.assertEqual(company.name, 'Example Company')

    def test_employee_model(self):
        employee = EmployeeModel.objects.get(user=self.user)
        self.assertEqual(employee.user.username, 'john_doe')
        self.assertEqual(employee.company.name, 'Example Company')
        self.assertEqual(employee.phone, '1234567890')
        self.assertEqual(employee.designation, 'Developer')

    def test_device_model(self):
        device = DeviceModel.objects.get(name='Test Device')
        self.assertEqual(device.name, 'Test Device')
        self.assertEqual(device.description, 'Test Description')

    def test_device_log_model(self):
        device_log = DeviceLogModel.objects.get(device=self.device)
        self.assertEqual(device_log.device.name, 'Test Device')
        self.assertEqual(device_log.employee.user.username, 'john_doe')
        self.assertEqual(device_log.check_out_date, self.check_out_date)
        self.assertEqual(device_log.condition_on_check_out, 'Good')

        device_log.condition_on_check_in = 'OK'
        device_log.save()

        updated_device_log = DeviceLogModel.objects.get(device=self.device)
        self.assertEqual(updated_device_log.condition_on_check_in, 'OK')
