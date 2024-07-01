from django.urls import path
from .views import CurrentUserApiView


urlpatterns = [
    path('current_user/', CurrentUserApiView.as_view(), name='current_user'),
]
