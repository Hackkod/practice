from rest_framework import serializers
from .models import StudentForm, MentorForm
from hardskillApp.serializers import HardSkillSerializer


output_fields = [
            'surname',
            'name',
            'patronymic',
            'gender',
            'birth_date',
            'soft_skills',
            'hard_skills_id',
            'hard_skills_ids',
            'other_info',
        ]


class StudentFormSerializer(serializers.ModelSerializer):
    hard_skills_ids = HardSkillSerializer(
        many=True,
        read_only=True,
        source='hard_skills_id'
    )

    class Meta:
        model = StudentForm
        extra_kwargs = {'hard_skills_id': {'write_only': True},
                        'course': {'read_only': True}}
        fields = output_fields + [
            'establishment',
            'start_study_year',
            'end_study_year',
            'course',
        ]


class MentorFormSerializer(serializers.ModelSerializer):
    hard_skills_ids = HardSkillSerializer(
        many=True,
        read_only=True,
        source='hard_skills_id'
    )

    class Meta:
        model = MentorForm
        extra_kwargs = {'hard_skills_id': {'write_only': True}}
        fields = output_fields + ['job_position']
