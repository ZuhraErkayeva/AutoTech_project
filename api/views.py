from rest_framework.viewsets import ModelViewSet
from .models import Vehicles, Sensors, Service_centers, Maintenance
from .serializers import ServiceSerializer,VehiclesSerializer,SensorsSerializer,MaintenanceSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service_centers.objects.all()
    serializer_class = ServiceSerializer


