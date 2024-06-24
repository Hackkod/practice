from django.db import models
from utils.models import EventBase
from anketApp.models import StudentAnket, MentorAnket


class PracticeOrInternship(EventBase):
    PRACTICE_OR_INTERNSHIP_CHOICES = [
        ('PRACTICE', 'Practice'),
        ('INTERNSHIP', 'Internship')
    ]

    student = models.ForeignKey(
        StudentAnket,
        on_delete=models.CASCADE,
        related_name='pi_student'
    )
    mentor = models.ForeignKey(
        MentorAnket,
        on_delete=models.CASCADE,
        related_name='pi_mentor'
    )
    type = models.CharField(
        max_length=20,
        choices=PRACTICE_OR_INTERNSHIP_CHOICES
    )

    def __str__(self):
        return f'{self.name}: {self.student}'


class Work(EventBase):
    WORK_TYPE_CHOICES = [
        ('AGREEMENT', 'Agreement'),
        ('STAFF', 'Staff')
    ]

    student = models.ForeignKey(
        StudentAnket,
        on_delete=models.CASCADE,
        related_name='work_student'
    )
    mentor = models.ForeignKey(
        MentorAnket,
        on_delete=models.CASCADE,
        related_name='work_mentor'
    )
    type = models.CharField(
        max_length=20,
        choices=WORK_TYPE_CHOICES
    )
    position = models.CharField(
        max_length=1024
    )

    def __str__(self):
        return f'{self.name}: {self.student}'
