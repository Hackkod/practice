from django.urls import path
from rest_framework import routers
from .views import StudentAnketViewSet, MentorAnketViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentAnketViewSet)
router.register(r'mentors', MentorAnketViewSet)

urlpatterns = router.urls
