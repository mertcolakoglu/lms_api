from django.urls import path
from .views import ProfileRetrieveUpdateAPIView

urlpatterns = [
    path('me/', ProfileRetrieveUpdateAPIView.as_view(), name='profile-detail'),
]