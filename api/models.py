from django.db import models

class Vehicles(models.Model):
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    vin = models.IntegerField()

    def __str__(self):
        return self.model



