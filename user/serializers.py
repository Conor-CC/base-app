from user.models import User, UserTypeOne
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer_Create(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    organization = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'organization', 'user_type']

    def create(self, validated_data):
        user_obj = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            organization=validated_data['organization'],
            user_type=validated_data['user_type']
        )
        user_obj.set_password(validated_data['password1'])
        return user_obj


class UserSerializer_RetrieveUpdateDestroy(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name',
                  'last_name', 'organization', 'user_type']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    def validate_email(self, email):
        # Validation Logic
        return email

    def validate_password(self, password):
        return password

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
        }

    def save(self):
        user = super().create(self.validated_data)
        return user


class UserSerializer_List(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'user_type', 'first_name',
                  'last_name', 'organization', 'created_on', 'updated_on']


# UserTypeOne Serializers =====================================================

class UserTypeOneSerializer_Create(serializers.ModelSerializer):
    user = UserSerializer_Create(required=True)

    class Meta:
        model = UserTypeOne
        fields = ['user', 'info_user_type_one']

    def validate_info_user_type_one(self, info_user_type_one):
        # Also see Object Level Validation, looks tidier: https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        if 'key_info' not in info_user_type_one.lower():
            raise serializers.ValidationError("String \"key_info\" must be in info_user_type_one")
        return info_user_type_one

    def create(self, validated_data):
        user_data = validated_data['user']
        user_data['user_type'] = User.USER_TYPE_ONE
        user_obj = UserSerializer_Create.create(UserSerializer_Create,
                                                validated_data=user_data)
        user_obj.save()
        userTypeOne = UserTypeOne(
                                  user=user_obj,
                                  info_user_type_one=validated_data['info_user_type_one']
                                 )
        userTypeOne.save()
        return userTypeOne

    def save(self, request):
        return self.create(self.validated_data)


class UserTypeOneSerializer_List(serializers.ModelSerializer):
    user = UserSerializer_List(required=True)

    class Meta:
        model = UserTypeOne
        fields = ['user', 'info_user_type_one']

    def validate_info_user_type_one(self, info_user_type_one):
        # Also see Object Level Validation, looks tidier: https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        if 'key_info' not in info_user_type_one.lower():
            raise serializers.ValidationError("String \"key_info\" must be in info_user_type_one")
        return info_user_type_one

    def update(self, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserTypeOneSerializer_RetrieveUpdateDestroy(serializers.ModelSerializer):
    user = UserSerializer_RetrieveUpdateDestroy(required=True)

    class Meta:
        model = UserTypeOne
        fields = ['user', 'info_user_type_one']

    def validate_info_user_type_one(self, info_user_type_one):
        # Also see Object Level Validation, looks tidier: https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        if 'key_info' not in info_user_type_one.lower():
            raise serializers.ValidationError("String \"key_info\" must be in info_user_type_one")
        return info_user_type_one

    def update(self, validated_data):
        pass

    def create(self, validated_data):
        pass
