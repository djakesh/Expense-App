from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Account


class AccountRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('first_name',
                  'last_name',
                  'email',
                  'salary',
                  'password',
                  'password2')

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['email']).first()
        if user:
            raise ValidationError({'Error': 'Email already exist'})
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'Error': 'Passwords did not mactch'})
        return attrs

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['email'],
            password=make_password(validate_data['password'])
        )

        account = Account.objects.create(
            user=user,
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
            email=validate_data['email'],
            salary=validate_data['salary']
        )

        return account