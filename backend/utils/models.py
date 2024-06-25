from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )

    class Meta:
        abstract = True


class AnketBase(TimeStampedModel):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

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
        max_length=1,
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
        upload_to='images/%Y/%m/%d/'
    )

    class Meta:
        abstract = True


class EventBase(TimeStampedModel):
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
