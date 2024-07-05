from itertools import count
from django.shortcuts import render
from .models import courses, workshop

# Create your views here.

def index(request):
    courses_data = courses.objects.all()
    workshop_data = workshop.objects.all()
    return render(request, "mainsite/index.html",{"courses":courses_data, "workshop":workshop_data})