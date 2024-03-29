from django.contrib import admin
from app_main.models import (
    CompanyModel,
    EmployeeModel,
    DeviceModel,
    DeviceLogModel
)

# Register your models here.
admin.site.site_header = "Corporate Asset Tracking App"

admin.site.register(CompanyModel)

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('display_username', 'display_company_name', 'phone', 'designation',)
    search_fields = ['user__username', 'phone', 'designation']

    @admin.display(ordering='user__id', description='Name')
    def display_username(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username
    
    @admin.display(ordering='company__id', description='Company')
    def display_company_name(self, obj):
        return obj.company.name if obj.company.name else 'N/A'
    

admin.site.register(EmployeeModel, EmployeeModelAdmin)


class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

admin.site.register(DeviceModel, DeviceModelAdmin)


class DeviceLogModelAdmin(admin.ModelAdmin):
    list_display = ('display_device_name', 'display_employee_name', 'check_in_date', 'check_out_date', 'condition_on_check_in', 'condition_on_check_out')

    @admin.display(ordering='device__id', description='Device')
    def display_device_name(self, obj):
        return obj.device.name if obj.device.name else 'N/A'
    
    @admin.display(ordering='employee__id', description='Employee')
    def display_employee_name(self, obj):
        return obj.employee.user.get_full_name() if obj.employee.user.get_full_name() else obj.employee.user.username

admin.site.register(DeviceLogModel, DeviceLogModelAdmin)
