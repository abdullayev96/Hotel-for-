from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "guest", "number_of_adults", "number_of_childrens",
                    "start_date", "end_date", "booked_date", "confirmed_date", "status"]

admin.site.register(Order, OrderAdmin)
