from django.db import models


class HardSkill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
