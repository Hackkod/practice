from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentForm, MentorForm


class StudentFormView(viewsets.ModelViewSet):
    queryset = StudentForm.objects.all()
    serializer_class = StudentForm


class MentorFormView(viewsets.ModelViewSet):
    queryset = MentorForm.objects.all()
    serializer_class = MentorForm
