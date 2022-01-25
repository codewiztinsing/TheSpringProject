from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.views import Token
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = [
                    "first_name",
                    "last_name",
                    "email",
                    'cid'
                ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user