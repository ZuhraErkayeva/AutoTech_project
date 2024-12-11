from rest_framework.viewsets import ModelViewSet
from .models import Vehicles, Sensors, Service_centers, Maintenance
from .serializers import ServiceSerializer,VehiclesSerializer,SensorsSerializer,MaintenanceSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

