from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def user(request):
    return HttpResponse('User app')