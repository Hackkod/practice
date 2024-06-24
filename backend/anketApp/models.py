from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from utils.models import AnketBase
from hardSkillApp.models import HardSkill


class StudentAnket(AnketBase):
    hard_skills_id = models.ManyToManyField(
        HardSkill,
        related_name='sa_hard_skills_id',
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

    def save(self, *args, **kwargs):
        start_year = self.start_study_year
        end_year = self.end_study_year
        if end_year < start_year:
            raise ValidationError('Старт обучения не может быть после его конца')
        if start_year and end_year and (end_year - start_year) < 4:
            raise ValidationError('Срок обучения должен составлять не менее 4-х лет')
        curr_date = datetime.date.today()
        if start_year > curr_date.year or (start_year == curr_date.year and curr_date.month < 9):
            raise ValidationError('Старт обучения не может быть в будущем')
        if curr_date.month < 9:
            self.course = curr_date.year - start_year
        else:
            self.course = curr_date.year - start_year + 1
        super().save(*args, **kwargs)

    def valid(self):
        pass

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class MentorAnket(AnketBase):
    hard_skills_id = models.ManyToManyField(
        HardSkill,
        related_name='ma_hard_skills_id',
    )
    job_position = models.CharField(
        max_length=1024
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
