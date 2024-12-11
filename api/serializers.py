from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Vehicles, Sensors, Service_centers, Maintenance

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('model', 'year', 'vin')


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ('SENSOR_TYPES', 'installed_date', 'type', 'vehicles')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_centers
        fields = ('name', 'address', 'phone', 'rating')


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('SERVICE_TYPES', 'vehicle', 'service_type', 'scheduled_date')


    def validate_scheduled_date(self, obj):
        a = obj.get('scheduled_date')
        today = date.today()
        if a > today:
            raise ValidationError('Xizmat rejalashtirilgan sana xato')
        return obj.data