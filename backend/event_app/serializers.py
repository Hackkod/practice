from rest_framework import serializers
from .models import Study, Work
from anket_app.serializers import MentorAnketSerializer, StudentAnketSerializer


output_fields = [
            'id',
            'name',
            'start_date',
            'end_date',
            'description',
            'student',
            'student_full',
            'mentor',
            'mentor_full',
            'type',
        ]


class StudySerializer(serializers.ModelSerializer):
    mentor_full = MentorAnketSerializer(
        read_only=True,
        source='mentor',
    )
    student_full = StudentAnketSerializer(
        read_only=True,
        source='student',
    )

    class Meta:
        model = Study
        extra_kwargs = {
            'mentor': {'write_only': True},
            'student': {'write_only': True}
        }
        fields = output_fields


class WorkSerializer(serializers.ModelSerializer):
    mentor_full = MentorAnketSerializer(
        read_only=True,
        source='mentor',
    )
    student_full = StudentAnketSerializer(
        read_only=True,
        source='student',
    )

    class Meta:
        model = Work
        extra_kwargs = {
            'mentor': {'write_only': True},
            'student': {'write_only': True}
        }
        fields = output_fields + ['position']
