from django.http import HttpResponse
# from django.shortcuts import render

from .models import Measurement

# Create your views here.
def index(request):
    return HttpResponse("Hello, you're at the pm index.")

def save(request):
    return HttpResponse("Hello, you're at the save view.")
