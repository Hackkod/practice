from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentAnket, MentorAnket
from .serializers import StudentAnketSerializer, MentorAnketSerializer


class StudentAnketViewSet(viewsets.ModelViewSet):
    queryset = StudentAnket.objects.all()
    serializer_class = StudentAnketSerializer


class MentorAnketViewSet(viewsets.ModelViewSet):
    queryset = MentorAnket.objects.all()
    serializer_class = MentorAnketSerializer
