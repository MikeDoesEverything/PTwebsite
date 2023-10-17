from django.shortcuts import render
from django.http import HttpResponse

def training_plans(request):
    return render(request, "training_plans.html")

# Create your views here.
