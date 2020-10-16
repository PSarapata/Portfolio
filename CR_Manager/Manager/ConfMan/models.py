from django.db import models
from django.utils.timezone import now


class Room(models.Model):
    name = models.TextField(max_length=255, unique=True)
    capacity = models.PositiveSmallIntegerField(null=False)
    has_projector = models.NullBooleanField(default="No data")

    def get_absolute_url(self):
        return "/room/detail/%s/" % self.pk


class Reservation(models.Model):
    date = models.DateField(default=now())
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('date', 'room_id')
