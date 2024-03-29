from django.contrib import admin
from app_main.models import (
    CompanyModel,
    EmployeeModel,
    DeviceModel,
    DeviceLogModel
)

# Register your models here.
admin.site.site_header = "Track Corporate Assets"

admin.site.register(CompanyModel)

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('display_username', 'display_company_name', 'phone', 'designation',)
    search_fields = ['name', 'model',]

    @admin.display(ordering='user__id', description='Name')
    def display_username(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username
    
    @admin.display(ordering='company__id', description='Company')
    def display_company_name(self, obj):
        return obj.company.name if obj.company.name else 'N/A'
    

admin.site.register(EmployeeModel, EmployeeModelAdmin)

admin.site.register(DeviceModel)
admin.site.register(DeviceLogModel)
