from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/anketApp/', include('anketApp.urls')),
    path('api/eventApp/', include('eventApp.urls')),
    path('api/hardskillApp/', include('hardskillApp.urls')),
]
