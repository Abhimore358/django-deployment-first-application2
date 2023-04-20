from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f11(request):
    return HttpResponse("<h1>Hello, Good Morning User....!!! Have A Nice day... </h1><hr/>")