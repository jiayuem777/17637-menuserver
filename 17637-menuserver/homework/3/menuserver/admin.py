from django.contrib import admin
from .models import Dishes, Stores, Managers, Employees, Orders, SubmittedOrders

# Register your models here.
admin.site.register(Dishes)
admin.site.register(Stores)
admin.site.register(Managers)
admin.site.register(Employees)
admin.site.register(Orders)
admin.site.register(SubmittedOrders)
