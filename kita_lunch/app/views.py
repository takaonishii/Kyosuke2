from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Store,Area

class TopView(ListView):
    template_name = "top.html"
    model = Area

class StoreListView(ListView):
     model = Store
