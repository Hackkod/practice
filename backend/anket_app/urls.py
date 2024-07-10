from django.urls import path
from rest_framework import routers
from .views import StudentAnketViewSet, MentorAnketViewSet, DownloadFileView

router = routers.DefaultRouter()
router.register(r'students', StudentAnketViewSet)
router.register(r'mentors', MentorAnketViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('download/', DownloadFileView.as_view(), name='download_file'),
]
