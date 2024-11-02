# from django.shortcuts import render

# from django.shortcuts import render
# from django.views.generic import TemplateView, ListView
# from .models import Store,Area

# class TopView(ListView):
#     template_name = "top.html"
#     model = Area

# class StoreListView(ListView):
#      model = Store
#      template_name = "store_list.html"

from django.shortcuts import render			
from django.views import generic			
from .models import Area, Store			
			
# Create your views here.			
class AreaStoreListView(generic.ListView):			
			
    model = Store			
    template_name = "store_list.html"			
    context_object_name = "stores"			
			
def get_queryset(self):			
    area_id = self.kwargs["area_id"]			
    return Store.objects.filter(areastore__area_id = area_id)			
			
def get_context_data(self, **kwargs):			
    context = super().get_context_data(**kwargs)			
    context["area"] = Area.objects.get(area_id=self.kwargs["area_id"])			
    return context			