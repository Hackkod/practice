from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Work, Study
from .serializers import WorkSerializer, StudySerializer
from rest_framework.pagination import PageNumberPagination


class WorkStudyPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = WorkStudyPagination


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    pagination_class = WorkStudyPagination
