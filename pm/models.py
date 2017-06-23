from django.db import models

# Create your models here.
class Measurement(models.Model):
    time = models.DateTimeField('date & time')
    lat = models.DecimalField('latitude', max_digits=8, decimal_places=6)
    lon = models.DecimalField('longitude', max_digits=8, decimal_places=6)
    ele = models.DecimalField('elevation', max_digits=5, decimal_places=1)
    pm25 = models.DecimalField('PM2.5', max_digits=4, decimal_places=1)
    pm10 = models.DecimalField('PM10', max_digits=4, decimal_places=1)

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)