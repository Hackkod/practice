from django.db import models
from utils.models import FormBase
from hardskillApp.models import HardSkill


class StudentForm(FormBase):
    hard_skills_id = models.ManyToManyField(HardSkill)
    establishment = models.CharField(max_length=1024)
    start_study_date = models.DateField()
    end_study_date = models.DateField()
    course = models.IntegerField()

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class MentorForm(FormBase):
    hard_skills_id = models.ManyToManyField(HardSkill)
    job_position = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
