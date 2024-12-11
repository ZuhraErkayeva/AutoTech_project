from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Vehicles, Sensors, Service_centers, Maintenance

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('id','model', 'year', 'vin')


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ('id', 'installed_date', 'type', 'vehicles')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_centers
        fields = ('id','name', 'address', 'phone', 'rating')


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'vehicle', 'service_type', 'scheduled_date')


    def validate_scheduled_date(self, value):
        today = date.today()
        if value <= today:
            raise ValidationError('Xizmat rejalashtirilgan sana xato')
        return value