from django.urls import path
from .views import AccountRegistrationAPIView

urlpatterns = [
    path('register/',AccountRegistrationAPIView.as_view(), name='register'),
]