from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import datetime
import uuid

PHONE_REGEX = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


# Should contain fields common to all users that are AUTOMATICALLY generated

class UserModel_Root(models.Model):
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        now = datetime.datetime.now(datetime.timezone.utc)
        if not self.created_on and not self.id:
            self.created_on = now
        self.updated_on = now
        super(UserModel_Root, self).save()


# Should contain fields common to all users that are MANUALLY configured

class UserModel_Base(AbstractUser, UserModel_Root):
    USER_TYPE_ONE = 'U1'
    USER_TYPE_TWO = 'U2'
    USER_TYPE_THREE = 'U3'
    ADMIN = 'AD'
    USER_TYPE_CHOICES = [
        (USER_TYPE_ONE, 'user_type_one'),
        (USER_TYPE_TWO, 'user_type_two'),
        (USER_TYPE_THREE, 'user_type_three'),
        (ADMIN, 'admin')
    ]
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    organization = models.CharField(max_length=32)
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_ONE
    )


# User profiles, all should contain information UNIQUE to the type of user

class UserModel_ProfileTypeOne(models.Model):
    user = models.OneToOneField(UserModel_Base, on_delete=models.CASCADE, primary_key=True)
    info_user_type_one = models.CharField(max_length=30)


class UserModel_ProfileTypeTwo(models.Model):
    user = models.OneToOneField(UserModel_Base, on_delete=models.CASCADE, primary_key=True)
    info_user_type_two = models.CharField(max_length=30)


class UserModel_ProfileTypeThree(models.Model):
    user = models.OneToOneField(UserModel_Base, on_delete=models.CASCADE, primary_key=True)
    info_user_type_three = models.CharField(max_length=30)
