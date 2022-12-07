from django.contrib import admin
from . import models

# Register your models here.


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'capacity']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'status']

class RoomImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'image']


admin.site.register(models.RoomType, RoomTypeAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.RoomImage, RoomImageAdmin)