from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/anket_app/', include('anket_app.urls')),
    path('api/event_app/', include('event_app.urls')),
    path('api/hard_skill_app/', include('hard_skill_app.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/user_app/', include('user_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
