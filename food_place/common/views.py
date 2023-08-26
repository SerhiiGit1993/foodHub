from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def common(request):
    return HttpResponse('Common app')