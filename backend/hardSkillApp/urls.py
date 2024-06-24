from rest_framework import routers
from .views import HardSkillListViewSet

router = routers.DefaultRouter()
router.register(r'hard_skills', HardSkillListViewSet)

urlpatterns = router.urls
