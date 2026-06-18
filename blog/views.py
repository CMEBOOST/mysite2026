from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World<h1>This is 10.80.22.31</h1><h2>Surachet 67114540583</h2>")

