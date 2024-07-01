from django.shortcuts import render
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework.views import APIView


class CurrentUserApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)
    