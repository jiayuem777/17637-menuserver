from django.contrib import admin
from .models import Dishes, Stores, Orders, SubmittedOrders, Roles

# Register your models here.
admin.site.register(Dishes)
admin.site.register(Stores)
admin.site.register(Roles)
admin.site.register(Orders)
admin.site.register(SubmittedOrders)
