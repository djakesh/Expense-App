from .serializers import AccountRegistrationSerializer
from rest_framework import generics
from .models import Account


class AccountRegistrationAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer

