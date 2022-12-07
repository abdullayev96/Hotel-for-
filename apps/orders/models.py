from django.db import models
from apps.rooms.models import  *


class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    guest=models.ForeignKey(RoomImage,null=True, blank=True,  on_delete=models.SET_NULL)
    number_of_adults = models.IntegerField(max_length=300, verbose_name="Number_of_adults")
    number_of_children = models.IntegerField(max_length=300, verbose_name="Number_of_childers")
    additional = models.CharField(max_length=200, null=False, blank=False)
    room=models.ForeignKey(Room,  null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField(max_length=50)
    end_date = models.DateTimeField(max_length=100)
    booked_date = models.DateField(max_length=200)
    confirmed_date = models.DateField(max_length=200)
    status = models.CharField(max_length=100,choices=ROOM_STATUS, confirmed_date="Home" , active="Now", completed="new_house", verbose_name="Status")

    def __str__(self):
        return self.status





