from rest_framework import serializers
from .models import PracticeOrInternship, Work
from anketApp.serializers import MentorFormSerializer, StudentFormSerializer


output_fields = [
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


class PracticeOrInternshipSerializer(serializers.ModelSerializer):
    mentor_full = MentorFormSerializer(
        read_only=True,
        source='mentor',
    )
    student_full = StudentFormSerializer(
        read_only=True,
        source='student',
    )

    class Meta:
        model = PracticeOrInternship
        extra_kwargs = {
            'mentor': {'write_only': True},
            'student': {'write_only': True}
        }
        fields = output_fields


class WorkSerializer(serializers.ModelSerializer):
    mentor_full = MentorFormSerializer(
        read_only=True,
        source='mentor',
    )
    student_full = StudentFormSerializer(
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
