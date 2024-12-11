from django.db import models

class Vehicles(models.Model):
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    vin = models.IntegerField()

    def __str__(self):
        return self.model

class Sensors(models.Model):
    SENSOR_TYPES = [
        ('oil', 'Moy almashtirish'),
        ('gasoline', 'Benzin quyish'),
        ('temperature', 'Dvigatel harorati')
    ]

    installed_date = models.DateTimeField(auto_now_add=True)
    vehicles = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=SENSOR_TYPES)

    def __str__(self):
        return self.type


class Service_centers(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name


 class Maintenance(models.Model):
    SERVICE_TYPES = [
        ('oil_change', 'Moy almashtirish'),
        ('gasoline_refill', 'Benzin quyish'),
        ('engine_temp', 'Dvigatel harorati')
    ]

    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100, choices=SERVICE_TYPES)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.scheduled_date


