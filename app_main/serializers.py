from rest_framework import serializers
from django.contrib.auth.models import User

from app_main.models import (
    CompanyModel,
    EmployeeModel,
    DeviceModel,
    DeviceLogModel
)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


    def validate_password(self, value):
        if value is not None and value.strip() == '':
            raise serializers.ValidationError("Password cannot be empty")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Checking if password is provided and update it
        password = validated_data.get('password')
        if password is not None and password.strip() != '':
            instance.set_password(password)
            instance.save()
        else:
            instance.save(update_fields=['username', 'email', 'first_name', 'last_name'])
        
        return instance
    


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ['id', 'name',]
        extra_kwargs = {'name': {'required': True}}


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'user', 'company', 'phone', 'designation']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ['id', 'name', 'description']


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLogModel
        fields = ['id', 'device', 'employee', 'check_out_date', 'check_in_date', 'condition_on_check_out', 'condition_on_check_in']