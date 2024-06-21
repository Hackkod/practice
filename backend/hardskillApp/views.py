from django.shortcuts import render
from rest_framework import viewsets
from .models import HardSkill
from .serializers import HardSkillSerializer


class HardSkillListViewSet(viewsets.ModelViewSet):
    queryset = HardSkill.objects.all()
    serializer_class = HardSkillSerializer
