from rest_framework import routers
from .views import WorkViewSet, PracticeOrInternshipViewSet

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)
router.register(r'studies', PracticeOrInternshipViewSet)

urlpatterns = router.urls
