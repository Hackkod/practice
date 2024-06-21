from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import StudentFormViewSet, MentorFormViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentFormViewSet)
router.register(r'mentors', MentorFormViewSet)

urlpatterns = router.urls
