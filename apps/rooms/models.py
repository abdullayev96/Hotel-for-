from django.db import models
from django.utils.translation import gettext_lazy as _

ROOM_STATUS = (
    ('empty', _('Empty')),
    ('busy', _('Busy')),
    ('booked', _('Booked'))
)


class RoomType(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name=_("Type")
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=50,
        verbose_name=_("Price")
    )

    capacity = models.IntegerField(
        default=0,
        verbose_name=_("Capacity")
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    type = models.ForeignKey(
        to=RoomType,
        on_delete=models.CASCADE,
        verbose_name=_("Type")
    )

    number = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Number")
    )

    status = models.CharField(
        max_length=10,
        choices=ROOM_STATUS,
        default='empty',
        verbose_name=_("Status")
    )

    description = models.TextField(
        verbose_name=_("Description")
    )

    def __str__(self):
        return f"{self.type} || {self.status}"

class RoomImage(models.Model):
    id=models.UUIDField(primary_key=True)
    room=models.ForeignKey(to=Room,on_delete=models.CASCADE,verbose_name=_("Type"))
    image=models.FileField(upload_to="RoomImage", null=True, blank=True)




