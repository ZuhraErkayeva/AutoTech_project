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


