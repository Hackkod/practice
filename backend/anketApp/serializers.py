from rest_framework import serializers

from .models import StudentAnket, MentorAnket
from hardSkillApp.serializers import HardSkillSerializer


output_fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'gender',
            'birth_date',
            'soft_skills',
            'hard_skills_id',
            'hard_skills_ids',
            'other_info',
            'profile_photo'
        ]


class StudentAnketSerializer(serializers.ModelSerializer):
    hard_skills_ids = HardSkillSerializer(
        many=True,
        read_only=True,
        source='hard_skills_id'
    )

    class Meta:
        model = StudentAnket
        extra_kwargs = {'hard_skills_id': {'write_only': True},
                        'course': {'read_only': True}}
        fields = output_fields + [
            'establishment',
            'start_study_year',
            'end_study_year',
            'course',
        ]


class MentorAnketSerializer(serializers.ModelSerializer):
    hard_skills_ids = HardSkillSerializer(
        many=True,
        read_only=True,
        source='hard_skills_id'
    )

    class Meta:
        model = MentorAnket
        extra_kwargs = {'hard_skills_id': {'write_only': True}}
        fields = output_fields + ['job_position']
