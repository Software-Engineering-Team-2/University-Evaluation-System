from rest_framework import serializers
from users.models import CustomUser
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from .models import USER_TYPES
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    # usertype = serializers.ChoiceField(choices=USER_TYPES)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        # user.usertype = self.data.get('usertype')
        user.save()
        return user

class CustomLoginSerializer(LoginSerializer):
    
    def validate_auth_user_status(self, user):
        if not user.is_active or not user.verified:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'first_name',
            'last_name',
            'usertype'
        )
        read_only_fields = ('pk', 'email', 'first_name', 'last_name','usertype')