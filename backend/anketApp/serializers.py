from rest_framework import serializers
from .models import StudentForm, MentorForm
from hardskillApp.serializers import HardSkillSerializer


class StudentFormSerializer(serializers.ModelSerializer):
    hard_skills_ids = HardSkillSerializer(
        many=True,
        read_only=True,
        source='hard_skills_id'
    )

    class Meta:
        model = StudentForm
        extra_kwargs = {'hard_skills_id': {'write_only': True}}
        fields = [
            'surname',
            'name',
            'patronymic',
            'gender',
            'birth_date',
            'soft_skills',
            'hard_skills_id',
            'hard_skills_ids',
            'establishment',
            'start_study_date',
            'end_study_date',
            'course',
            'other_info',
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
        fields = [
            'surname',
            'name',
            'patronymic',
            'gender',
            'birth_date',
            'soft_skills',
            'hard_skills_id',
            'hard_skills_ids',
            'job_position',
            'other_info',
        ]
