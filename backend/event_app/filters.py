import django_filters
from .models import Work, Study, STUDY_TYPE_CHOICES, WORK_TYPE_CHOICES


class WorkFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    type = django_filters.ChoiceFilter(choices=WORK_TYPE_CHOICES)

    class Meta:
        model = Work
        fields = ['start_date', 'end_date', 'type']


class StudyFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    type = django_filters.ChoiceFilter(choices=STUDY_TYPE_CHOICES)

    class Meta:
        model = Study
        fields = ['start_date', 'end_date', 'type']
