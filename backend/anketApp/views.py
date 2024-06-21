from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentForm, MentorForm
from .serializers import StudentFormSerializer, MentorFormSerializer


class StudentFormViewSet(viewsets.ModelViewSet):
    queryset = StudentForm.objects.all()
    serializer_class = StudentFormSerializer


class MentorFormViewSet(viewsets.ModelViewSet):
    queryset = MentorForm.objects.all()
    serializer_class = MentorFormSerializer
