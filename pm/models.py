from django.db import models

# Create your models here.
class Measurement(models.Model):
    time = models.DateTimeField('date & time')
    lat = models.DecimalField('latitude', max_digits = 8, decimal_places = 6, null = True)
    lon = models.DecimalField('longitude', max_digits = 8, decimal_places = 6, null = True)
    ele = models.DecimalField('elevation', max_digits = 5, decimal_places = 1, null = True)
    pm25 = models.DecimalField('PM2.5', max_digits=4, decimal_places=1)
    pm10 = models.DecimalField('PM10', max_digits=4, decimal_places=1)
    def __str__(self):
        s = "time = " + str(self.time) + ", lat = " + str(self.lat) + ", lon = " + str(self.lon) + ", ele = " + str(self.ele) + ", pm25 = " + str(self.pm25) + ", pm10 = " + str(self.pm10)
        return s

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)