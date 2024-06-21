from rest_framework import serializers
from .models import StudentForm, MentorForm


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorForm
        fields = '__all__'
