from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.utils.dateformat import format
from django.views.decorators.csrf import ensure_csrf_cookie
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

# ensure_csrf_cookie() decorator forces the 'save' view
# to send the CSRF cookie to the client.
@ensure_csrf_cookie
def save(request):
#    Saves data sent via POST. If request method is GET,
#    it doesn't perform anything, apart from sending back
#    the CSRF cookie.
    if request.method == 'GET':
        return HttpResponse("Sending CSRF cookie.")

    if request.method == 'POST':
        pm25Values = request.POST.getlist('pm25')
        pm10Values = request.POST.getlist('pm10')
        timeValues = request.POST.getlist('time')

        if len(pm25Values) != len(pm10Values) or len(pm25Values) != len(timeValues):
            raise ValueError("Number of PM 2.5 measurements differs from PM 10 measurements.")

        responseText = "Saved data recorded at"

        for pm25, pm10, time in zip(pm25Values, pm10Values, timeValues):
            #time = dateparse.parse_datetime(time)
            measurement = Measurement(time = time,
#                                     lat = lat,
#                                     lon = lon,
#                                     ele = ele,
                                      pm25 = pm25,
                                      pm10 = pm10)
            measurement.save()
            responseText += " " + str(time)

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
