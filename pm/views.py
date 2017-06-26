from django.http import HttpResponse
from django.template import loader
from django.utils import dateparse
# from django.shortcuts import render

from .models import Measurement

# Create your views here.
def index(request):
    latest_measurement_list = Measurement.objects.order_by('-time')[:20]
    template = loader.get_template('pm/index.html')
    context = {
        'latest_measurement_list': latest_measurement_list,
    }
    return HttpResponse(template.render(context, request))

def save(request):
    time = request.GET['time']
#    lat = request.GET['lat']
#    lon = request.GET['lon']
#    ele = request.GET['ele']
    pm25 = request.GET['pm25']
    pm10 = request.GET['pm10']


    time = dateparse.parse_datetime(time)

    measurement = Measurement(time = time,
#                              lat = lat,
#                              lon = lon,
#                              ele = ele,
                              pm25 = pm25,
                              pm10 = pm10)
    measurement.save()
    responseText = "Saved data recorded at " + str(time)
    return HttpResponse(responseText)