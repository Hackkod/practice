from django.db import models


male = 'Мужской'
female = 'Женский'

GENDER_CHOICES = [
    (male, 'Мужской'),
    (female, 'Женский')
]


class AnketBase(models.Model):
    surname = models.CharField(
        max_length=1024
    )
    name = models.CharField(
        max_length=1024
    )
    patronymic = models.CharField(
        max_length=1024
    )
    gender = models.CharField(
        max_length=7,
        choices=GENDER_CHOICES
    )
    birth_date = models.DateField()
    soft_skills = models.TextField(
        blank=True
    )
    other_info = models.TextField(
        blank=True
    )
    profile_photo = models.ImageField(
        upload_to='static/staticfiles/%Y/%m/%d/',
        default='static/staticfiles/default_user.jpg'
    )

    class Meta:
        abstract = True
