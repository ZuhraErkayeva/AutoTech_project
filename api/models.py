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




