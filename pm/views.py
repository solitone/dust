from django.http import HttpResponse
from django.template import loader
from django.utils import dateparse, timezone
from django.utils.dateformat import format
# from django.shortcuts import render

from .models import Measurement

import datetime, json

# Create your views here.
def chart(request):
    template = loader.get_template('pm/chart.html')
    return HttpResponse(template.render({}, request))

def index(request):
    latest_measurement_list = Measurement.objects.order_by('-time')[:10]
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

def pm25series(request):
    series = []
    latest_measurements = Measurement.objects.order_by('-time')[:20]
    for measurement in latest_measurements:
        series.append(
            [int(format(measurement.time, 'U'))*1000, float(measurement.pm25), float(measurement.pm10)]
        )
    return HttpResponse(json.dumps(series), content_type="application/json")

def pmseries(request):
    series = []
    time_24_hours_ago = timezone.now() - datetime.timedelta(days = 1)
    latest_measurements = Measurement.objects.filter(time__gte = time_24_hours_ago)
    for measurement in latest_measurements:
        series.append(
            [int(format(measurement.time, 'U'))*1000, float(measurement.pm25), float(measurement.pm10)]
        )
    return HttpResponse(json.dumps(series), content_type="application/json")
