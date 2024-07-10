from io import BytesIO
from django.http import HttpResponse
from docx import Document
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError
import datetime
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import StudentAnket, MentorAnket
from .serializers import StudentAnketSerializer, MentorAnketSerializer
from .filters import StudentAnketFilter, MentorAnketFilter
from utils.data_extraction import extract_data_study, extract_data_internship
from utils.replace import replace_bookmarks


class StudentMentorPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StudentAnketViewSet(viewsets.ModelViewSet):
    queryset = StudentAnket.objects.all().order_by('id')
    serializer_class = StudentAnketSerializer
    pagination_class = StudentMentorPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_class = StudentAnketFilter
    search_fields = [
        'surname',
        'name',
        'patronymic',
        'gender',
        'birth_date',
        'soft_skills',
        'other_info',
        'hard_skills_id__skill_name',
        'establishment',
        'start_study_year',
        'end_study_year',
        'course',
    ]

    def perform_create(self, serializer):
        self.validate_study_years(serializer.validated_data)
        serializer.save()

    def perform_update(self, serializer):
        self.validate_study_years(serializer.validated_data)
        serializer.save()

    def validate_study_years(self, validated_data):
        start_year = validated_data.get('start_study_year')
        end_year = validated_data.get('end_study_year')

        if start_year and end_year:
            if end_year < start_year:
                raise ValidationError('Старт обучения не может быть после его конца')
            if (end_year - start_year) < 4:
                raise ValidationError('Срок обучения должен составлять не менее 4-х лет')
            elif (end_year - start_year) > 6:
                raise ValidationError('Срок обучения должен составлять не более 6-ти лет')

        curr_date = datetime.date.today()
        if start_year > curr_date.year or (start_year == curr_date.year and curr_date.month < 9):
            raise ValidationError('Старт обучения не может быть в будущем')

        if curr_date.year > end_year or curr_date.year == end_year and curr_date.month > 8:
            course = end_year - start_year
        elif curr_date.month < 9:
            course = curr_date.year - start_year
        else:
            course = curr_date.year - start_year + 1

        validated_data['course'] = course


class MentorAnketViewSet(viewsets.ModelViewSet):
    queryset = MentorAnket.objects.all().order_by('id')
    serializer_class = MentorAnketSerializer
    pagination_class = StudentMentorPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_class = MentorAnketFilter
    search_fields = [
        'surname',
        'name',
        'patronymic',
        'gender',
        'birth_date',
        'soft_skills',
        'other_info',
        'hard_skills_id__skill_name',
        'job_position'
    ]


class DownloadFileView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.data.get('type', '') == 'Практика':
            extracted_data = extract_data_study(request)

            template_path = 'static/staticfiles/study_template.docx'
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

            template_path = 'static/staticfiles/internship_template.docx'
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
