import django_filters

from hard_skill_app.models import HardSkill
from .models import StudentAnket, MentorAnket


class MultipleHardSkillsFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


hard_skills_id = django_filters.ModelMultipleChoiceFilter(
    field_name='hard_skills_id',
    to_field_name='id',
    queryset=HardSkill.objects.all()
)


class StudentAnketFilter(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name='course')

    class Meta:
        model = StudentAnket
        fields = ['hard_skills_id', 'course']


class MentorAnketFilter(django_filters.FilterSet):
    class Meta:
        model = MentorAnket
        fields = ['hard_skills_id']
