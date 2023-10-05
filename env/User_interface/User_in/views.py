from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, UserProfile, OtherUserData
from .serializers import CustomUserSerializer, UserProfileSerializer, OtherUserDataSerializer
from django.shortcuts import get_object_or_404

class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class CustomUserLoginView(APIView):
    def post(self, request):
        # Реализуйте вход пользователя здесь
        # Верните токен доступа или другой метод аутентификации
        pass

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class OtherUserDataDetailView(generics.RetrieveUpdateAPIView):
    queryset = OtherUserData.objects.all()
    serializer_class = OtherUserDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
