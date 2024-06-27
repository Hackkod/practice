from django.shortcuts import render
from rest_framework import viewsets
from .models import Work, Study
from .serializers import WorkSerializer, StudySerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
