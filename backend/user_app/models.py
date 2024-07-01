from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(
        upload_to='static/staticfiles/%Y/%m/%d/',
        default='static/staticfiles/user_admin.jpg'
    )
