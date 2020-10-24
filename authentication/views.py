from user.serializers import UserSerializer_RetrieveUpdateDestroy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer


class Login(APIView):

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # 'token' is the token object, 'created' is a boolean indicating if a
        # new token was created
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer_RetrieveUpdateDestroy(user)
        # Logic to retreive nested user fields/profiles perhaps here...
        # Design decision whether or not to do this with a seperate view
        # Maybe use: user_type = user_serializer.data['user_type']
        return Response({'token': token.key,
                         'user': user_serializer.data},
                        status=status.HTTP_200_OK)


class Logout(APIView):

    def post(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass
        return Response(status=status.HTTP_200_OK)
