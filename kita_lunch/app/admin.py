from django.contrib import admin
from .models import Area
admin.site.register(Area)

from .models import Store
admin.site.register(Store)

from .models import AreaStore
admin.site.register(AreaStore)