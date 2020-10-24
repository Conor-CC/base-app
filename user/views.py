from user.models import UserModel_Base, UserModel_ProfileTypeOne
from user import serializers as ser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_auth.registration.views import RegisterView, VerifyEmailView
from django.conf import settings
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings


class UserView_List(generics.ListAPIView):
    """
    List all stored 'Monthly Repayment' Calculations
    """
    queryset = UserModel_Base.objects.all()
    serializer_class = ser.UserSerializer_List


# UserTypeOne Views ===========================================================

class UserTypeOneView_Create(RegisterView):
    """
    Create a UserTypeOne object and save it
    """
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create

    def perform_create(self, serializer):
        user_type_one_obj = serializer.save(request=self.request)
        user = user_type_one_obj.user
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        return user


class UserTypeOneView_List(generics.ListAPIView):
    """
    List all saved UserTypeOne objects
    """
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_RetrieveUpdateDestroy


class UserTypeOneView_RetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Retreive or update a specific UserTypeOne object by id
    """
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create


class UserTypeOneView_Destroy(generics.DestroyAPIView):
    """
    Delete a saved UserTypeOne object by id
    """
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create
