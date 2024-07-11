from django.urls import path
from rest_framework import routers
from .views import WorkViewSet, StudyViewSet, DownloadFileView

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)
router.register(r'studies', StudyViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('download/', DownloadFileView.as_view(), name='download_file'),
]
