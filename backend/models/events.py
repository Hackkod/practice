from django.db import models


class EventBase(models.Model):
    name = models.CharField(
        max_length=1024
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(
        blank=True
    )

    class Meta:
        abstract = True
