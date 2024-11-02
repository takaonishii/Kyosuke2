from django.contrib import admin

from .models import Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_id','area_name']
    list_filter = ['area_name']
admin.site.register(Area,AreaAdmin)



from .models import Store
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'store_id',
        'store_name',
        'address',
        'price'
   ]
admin.site.register(Store,StoreAdmin)



from .models import AreaStore
class AreaStoreAdmin(admin.ModelAdmin):
    list_display = [
        'area',
        'store',
    ]

admin.site.register(AreaStore,AreaStoreAdmin)
