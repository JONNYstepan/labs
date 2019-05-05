from django.shortcuts import render
from django import template

from django.http import HttpResponse


def home(request):
    return render(request, "static_handler.html")


def hello(request):
    return HttpResponse("<h4>Привет, Мир!</h4>")

# Create your views here.
