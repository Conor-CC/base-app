from django.test import TestCase
from django.db import IntegrityError, transaction
from ._test_base import TestBase
from user import models as m


class User_Model(TestCase):
    """ Test module for User model """

# TBI: Test model constraints, model creates, model updates, model destroys

    def setUp(self):
        self.user_a = TestBase.USER_A
        self.user_b = TestBase.USER_B
        self.user_c = TestBase.USER_C

    def create_user(self, data):
        return m.UserModel_Base.objects.create(**data)

    def get_user_by_id(self, id):
        try:
            return m.UserModel_Base.objects.get(id=id)
        except Exception as e:
            raise e

    def test_user_create_delete(self):
        """
        Test that a User Object can be Created, has all of its default
        attributes, attribute constraints and can be successfully deleted.
        """
        # Verify User Creation
        user_obj = self.create_user(self.user_a)
        user_a = self.get_user_by_id(user_obj.id)
        self.assertEqual(user_a, user_obj)

        # Verify unique fields functioning as expected
        with self.assertRaises(IntegrityError):
            tmp = self.user_b
            tmp['email'] = user_a.email
            # IntegrityError is wrapped by Transaction object, hence the need
            # for following line.
            # https://stackoverflow.com/questions/21458387/transactionmanagementerror-you-cant-execute-queries-until-the-end-of-the-atom
            with transaction.atomic():
                self.create_user(tmp)

        with self.assertRaises(IntegrityError):
            tmp = self.user_b
            tmp['email'] = user_a.email
            with transaction.atomic():
                self.create_user(tmp)

        try:
            user_a.created_on
            user_a.updated_on
            user_a.uuid
            user_a.username
            user_a.email
            user_a.user_type
            user_a.password
            user_a.first_name
            user_a.last_name
            user_a.organization
        except Exception as e:
            self.fail(e)

        user_a.delete()
        with self.assertRaises(m.UserModel_Base.DoesNotExist):
            m.UserModel_Base.objects.get(id=user_obj.id)

    def test_user_update(self):
        """
        Test that a User Object can be Updated, with default model constraints
        working as expected.
        """
        user_a = self.create_user(self.user_a)

        user_a.email = 'new_email@email.com'
        user_a.save()
        user_a = self.get_user_by_id(id=user_a.id)
        self.assertEqual(user_a.email, 'new_email@email.com')
