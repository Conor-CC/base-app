from django.contrib import admin
from user.models import (UserModel_Base, UserModel_ProfileTypeOne,
                         UserModel_ProfileTypeTwo, UserModel_ProfileTypeThree)


@admin.register(UserModel_Base)
class UserModel_BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'updated_on', 'uuid', 'username',
                    'email', 'first_name', 'last_name', 'organization',
                    'user_type')


@admin.register(UserModel_ProfileTypeOne)
class UserModel_ProfileTypeOneAdmin(admin.ModelAdmin):
    list_display = ('user', 'info_user_type_one')


@admin.register(UserModel_ProfileTypeTwo)
class UserModel_ProfileTypeTwoAdmin(admin.ModelAdmin):
    list_display = ('user', 'info_user_type_two')


@admin.register(UserModel_ProfileTypeThree)
class UserModel_ProfileTypeThreeAdmin(admin.ModelAdmin):
    list_display = ('user', 'info_user_type_three')
