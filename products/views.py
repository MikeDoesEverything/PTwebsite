from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def hello(request):
    return HttpResponse("hello")


def new(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def trainingplan(request, training_plan_id):
    return HttpResponse(training_plan_id)
