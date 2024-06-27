from django.db import models
from models.events import EventBase
from anket_app.models import StudentAnket, MentorAnket


practice = 'PRACTICE'
internship = 'INTERNSHIP'

STUDY_TYPE_CHOICES = [
    (practice, 'Practice'),
    (internship, 'Internship')
]


class Study(EventBase):
    student = models.ForeignKey(
        StudentAnket,
        on_delete=models.CASCADE,
        related_name='study_student'
    )
    mentor = models.ForeignKey(
        MentorAnket,
        on_delete=models.CASCADE,
        related_name='study_mentor'
    )
    type = models.CharField(
        max_length=20,
        choices=STUDY_TYPE_CHOICES
    )

    def __str__(self):
        return f'{self.name}: {self.student}'


agreement = 'AGREEMENT'
staff = 'STAFF'

WORK_TYPE_CHOICES = [
    (agreement, 'Agreement'),
    (staff, 'Staff')
]


class Work(EventBase):
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
