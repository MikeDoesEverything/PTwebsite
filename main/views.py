from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, "homepage.html")


def contact_us(request):
    return render(request, "contact_us.html")
