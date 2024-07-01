from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)
