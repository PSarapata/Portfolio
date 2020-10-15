from django.db import models


class Room(models.Model):
    name = models.TextField(max_length=255, unique=True)
    capacity = models.PositiveSmallIntegerField(null=False)
    has_projector = models.NullBooleanField(default="No data")

    def get_absolute_url(self):
        return "/rooms/%s/" % self.pk
