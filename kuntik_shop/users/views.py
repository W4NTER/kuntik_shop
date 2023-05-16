from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def plug(request):
    return HttpResponse("<h4>Registration page</h4>")
