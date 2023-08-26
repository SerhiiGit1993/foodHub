from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *

# Create your views here.
def item(request):
    items = Items.objects.all()
    paginator = Paginator(items, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'templates_item/item.html', {'title': 'products', 'items': items, 'page_obj': page_obj})