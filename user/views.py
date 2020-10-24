from user.models import UserModel_Base, UserModel_ProfileTypeOne
from user import serializers as ser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView_List(generics.ListAPIView):
    """
    List all stored 'Monthly Repayment' Calculations
    """
    permission_classes = [IsAuthenticated, ]
    queryset = UserModel_Base.objects.all()
    serializer_class = ser.UserSerializer_List


# UserTypeOne Views ===========================================================

class UserTypeOneView_Create(APIView):
    """
    Create a UserTypeOne object and save it
    """
    permission_classes = [AllowAny, ]
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create

    def post(self, request, format=None):
        user_data = self.request.data
        user_data['user']['user_type'] = UserModel_Base.USER_TYPE_ONE
        serializer = ser.UserTypeOneSerializer_Create(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'result': "UserTypeOne created"},
                            status=status.HTTP_201_CREATED)


class UserTypeOneView_List(generics.ListAPIView):
    """
    List all saved UserTypeOne objects
    """
    permission_classes = [IsAuthenticated, ]
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_RetrieveUpdateDestroy


class UserTypeOneView_RetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Retreive or update a specific UserTypeOne object by id
    """
    permission_classes = [IsAuthenticated, ]
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create


class UserTypeOneView_Destroy(generics.DestroyAPIView):
    """
    Delete a saved UserTypeOne object by id
    """
    permission_classes = [IsAuthenticated, ]
    queryset = UserModel_ProfileTypeOne.objects.all()
    serializer_class = ser.UserTypeOneSerializer_Create
