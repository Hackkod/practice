from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from .models import Work, Study
from .serializers import WorkSerializer, StudySerializer
from .filters import WorkFilter, StudyFilter


class WorkStudyPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all().order_by('id')
    serializer_class = WorkSerializer
    pagination_class = WorkStudyPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_class = WorkFilter
    search_fields = [
        'name',
        'start_date',
        'end_date',
        'description',
        'type',
        'position',
        'student__surname',
        'student__name',
        'student__patronymic',
        'mentor__surname',
        'mentor__name',
        'mentor__patronymic'
    ]


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all().order_by('id')
    serializer_class = StudySerializer
    pagination_class = WorkStudyPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_class = StudyFilter
    search_fields = [
        'name',
        'start_date',
        'end_date',
        'description',
        'type',
        'student__surname',
        'student__name',
        'student__patronymic',
        'mentor__surname',
        'mentor__name',
        'mentor__patronymic'
    ]
