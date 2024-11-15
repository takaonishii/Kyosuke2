from django.contrib import admin
from .models import *

class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_id','area_name']
    list_filter = ['area_name']
admin.site.register(Area,AreaAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'store_id',
        'store_name',
        'address',
        'price'
   ]
admin.site.register(Store,StoreAdmin)



class AreaStoreAdmin(admin.ModelAdmin):
    list_display = [
        'area',
        'store',
    ]
admin.site.register(AreaStore,AreaStoreAdmin)


admin.site.register(Tag)
admin.site.register(StoreTag)
