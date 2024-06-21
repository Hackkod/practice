from django.db import models
from utils.models import EventBase


class PracticeOrInternship(EventBase):
    PRACTICE_OR_INTERNSHIP_CHOICES = [
        ('PRACTICE', 'Practice'),
        ('INTERNSHIP', 'Internship')
    ]

    type = models.CharField(max_length=20, choices=PRACTICE_OR_INTERNSHIP_CHOICES)

    def __str__(self):
        pass


class Work(EventBase):
    WORK_TYPE_CHOICES = [
        ('AGREEMENT', 'Agreement'),
        ('STAFF', 'staff')
    ]

    type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    position = models.CharField(max_length=1024)

    def __str__(self):
        pass
