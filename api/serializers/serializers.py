# from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Group
from api.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'second_name',
            'last_name',
            'second_lastname',
            'email',
            'document',
            'picture',
            'is_active',
            'is_admin',
            'create',
            'modified',
            'password',
            'password_confirm',
        ]
    def get_password_confirm(self, obj):
        return obj.password


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name''description',]

