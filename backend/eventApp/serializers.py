from rest_framework import serializers
from .models import PracticeOrInternship, Work


class PracticeOrInternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeOrInternship
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
