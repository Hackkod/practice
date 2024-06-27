from rest_framework import routers
from .views import WorkViewSet, StudyViewSet

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)
router.register(r'studies', StudyViewSet)

urlpatterns = router.urls
