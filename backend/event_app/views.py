from io import BytesIO
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from docx import Document
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Work, Study
from .serializers import WorkSerializer, StudySerializer
from .filters import WorkFilter, StudyFilter
from utils.data_extraction import extract_data_study, extract_data_internship
from utils.replace import replace_bookmarks


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


class DownloadFileView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.data.get('type', '') == 'Практика':
            extracted_data = extract_data_study(request)

            template_path = 'utils/templates/study_template.docx'
            document = Document(template_path)

            replace_bookmarks(document, {
                'establishment': extracted_data['establishment'],
                'student': extracted_data['student'],
                'mentor': extracted_data['mentor'],
                'defaul': extracted_data['defaul'],
                'course': str(extracted_data['course']),
                'start': extracted_data['start_date'],
                'end': extracted_data['end_date'],
                'current': extracted_data['current']
            })
        else:
            extracted_data = extract_data_internship(request)

            template_path = 'utils/templates/internship_template.docx'
            document = Document(template_path)

            replace_bookmarks(document, {
                'student': extracted_data['student'],
                'mentor': extracted_data['mentor'],
                'start': extracted_data['start_date'],
                'end': extracted_data['end_date'],
                'current': extracted_data['current']
            })

        file_stream = BytesIO()
        document.save(file_stream)
        file_stream.seek(0)

        response = HttpResponse(
            file_stream,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=praktika_info.docx'
        return response
