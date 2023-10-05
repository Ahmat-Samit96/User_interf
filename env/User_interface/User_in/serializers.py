from rest_framework import serializers
from .models import CustomUser, UserProfile, OtherUserData

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio', 'profile_picture', 'date_of_birth')

class OtherUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherUserData
        fields = ('id', 'user', 'address', 'phone_number')
