from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Contact,CommingMessages,GoingMessages,CustomUser

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class CreatecontactSerializer(serializers.ModelSerializer):
    userscontact = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Contact
        fields = ('id','name','userscontact','nickname','phonenumber','dob','Language')

class CommingmessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommingMessages

class GoingmessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoingMessages

class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='User.id')
    class Meta:
        model = CustomUser
        fields = ('id','user','nickname','phonenumber','gender','location','dob','Language','image')

    