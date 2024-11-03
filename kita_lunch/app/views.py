from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Area, Store

# import logging

# logger = logging.getLogger("django")

# def index(request):
#     logger.info("indexを呼び出し")
#     return HttpResponse(status=200)

class TopView(ListView):
    template_name = "top.html"
    model = Area

class StoreListView(ListView):
     model = Store
     template_name = "store_list.html"

# 関数ベースのビュー
def area_store_list(request, area_id):

    print("area_id=", area_id)
    # area_id = request.GET.get("area_id")

    stores = Store.objects.filter(
        areastore__area_id = area_id)

    comment="""
上記内容により、以下のSQL文が実行されます。
SELECT 
    "Store_info"."store_id", 
    "Store_info"."store_name", 
    "Store_info"."address", 
    "Store_info"."phone_number", 
    "Store_info"."menu", 
    "Store_info"."price", 
    "Store_info"."photo", 
    "Store_info"."business_hours", 
    "Store_info"."map_link", 
    "Store_info"."payment_methods" 
FROM 
    "Store_info" 
INNER JOIN "Area_Store" ON ("Store_info"."store_id" = "Area_Store"."store_id") 
WHERE "Area_Store"."area_id" = area_id
"""

    context = {"object_list": stores}

    return render(request, "app/store_list.html", context)

# クラスベースのビュー			
class AreaStoreListView(ListView):
    model = Store	
    template_name = "store_list.html"			
    context_object_name = "stores"			
			
def get_queryset(self):			
    area_id = self.kwargs["area_id"]
    # logger.info("area_id=", area_id)	
    stores = Store.objects.filter(
        areastore__area_id = area_id)			
    print(stores)
    return stores

def get_context_data(self, **kwargs):			
    context = super().get_context_data(**kwargs)			
    context["area"] = Area.objects.get(area_id=self.kwargs["area_id"])			
    return context