from .serializers import AccountRegistrationSerializer
from rest_framework import generics
from .models import Account


class AccountRegistrationAPIView(generics.CreateAPIView):
    """
    This endpoint registers users based on the fields
    """
    serializer_class = AccountRegistrationSerializer

