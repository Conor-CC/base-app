from django.test import TestCase
from django.core import serializers
from rest_framework.test import APIClient
from ._test_base import TestBase
from user import models as m
from user import serializers as s

client = APIClient()


class User_Views(TestCase):
    """ Test User API endpoints and serializer validation """

    def setUp(self):
        self.user_a = self.create_user(TestBase.USER_A)
        self.user_b = self.create_user(TestBase.USER_B)
        self.user_c = self.create_user(TestBase.USER_C)

    def create_user(self, data):
        return m.UserModel_Base.objects.create(**data)

    def test_user_view_list(self):
        response = client.get('/user/list-user/', format='json')
        r_list = serializers.deserialize('json', response.data)
        s_list = s.UserSerializer_List(m.UserModel_Base.objects.all(), many=True)
        print(r_list)
        print("\n")
        print(s_list.data)
        # self.assertEqual(res.content, objs)
