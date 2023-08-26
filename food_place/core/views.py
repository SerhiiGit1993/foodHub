from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def core(request):
    return HttpResponse('Core app')