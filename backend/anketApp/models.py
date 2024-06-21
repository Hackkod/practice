from django.db import models
from utils.models import FormBase
from hardskillApp.models import HardSkill


class StudentForm(FormBase):
    hard_skills_id = models.ForeignKey(HardSkill, on_delete=models.RESTRICT)
    establishment = models.CharField(max_length=1024)
    start_study_date = models.DateField()
    end_study_date = models.DateField()
    course = models.IntegerField()

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class MentorForm(FormBase):
    job_position = models.CharField(max_length=1024)
    hard_skills_id = models.ForeignKey(HardSkill, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
