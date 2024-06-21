from django.shortcuts import render
from rest_framework import viewsets
from .models import Work, PracticeOrInternship
from .serializers import WorkSerializer, PracticeOrInternshipSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class PracticeOrInternshipViewSet(viewsets.ModelViewSet):
    queryset = PracticeOrInternship.objects.all()
    serializer_class = PracticeOrInternshipSerializer
