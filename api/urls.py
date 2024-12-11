from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet,ServiceViewSet,SensorViewSet,MaintenanceViewSet
router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet),
router.register(r'service', ServiceViewSet),
router.register(r'sensor', SensorViewSet),
router.register(r'maintenance', MaintenanceViewSet)

urlpatterns = router.urls