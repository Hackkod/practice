from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from models.ankets import AnketBase
from hard_skill_app.models import HardSkill


class StudentAnket(AnketBase):
    hard_skills_id = models.ManyToManyField(
        HardSkill,
        related_name='student_anket_hard_skills_id',
    )
    establishment = models.CharField(
        max_length=1024,
    )
    start_study_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
        default=None
    )
    end_study_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
        default=None
    )
    course = models.IntegerField()

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class MentorAnket(AnketBase):
    hard_skills_id = models.ManyToManyField(
        HardSkill,
        related_name='mentor_anket_hard_skills_id',
    )
    job_position = models.CharField(
        max_length=1024
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
