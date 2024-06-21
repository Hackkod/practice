from rest_framework import serializers
from .models import StudentForm, MentorForm


class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__'


class MentorFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorForm
        fields = '__all__'
