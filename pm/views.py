from django.http import HttpResponse
from django.utils import dateparse
# from django.shortcuts import render

from .models import Measurement

# Create your views here.
def index(request):
    return HttpResponse("Hello, you're at the pm index.")

def save(request):
    now = request.GET['now']
#    lat = request.GET['lat']
#    lon = request.GET['lon']
#    ele = request.GET['ele']
    pm25 = request.GET['pm25']
    pm10 = request.GET['pm10']


    time = dateparse.parse_datetime(now)

    measurement = Measurement(time = time,
#                              lat = lat,
#                              lon = lon,
#                              ele = ele,
                              pm25 = pm25,
                              pm10 = pm10)
    measurement.save()

    responseText = "Hello, you're at the save view.\n"
    responseText += "+++ now = " + str(now) + "\n"
    responseText += str(Measurement.objects.all())


    return HttpResponse(responseText)
