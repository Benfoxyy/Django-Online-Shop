from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer,CustomTokenRefreshSerializer
from .serializers import SignUpApiSerializers
from accounts.models import User


class SignUpApiView(GenericAPIView):
    serializer_class = SignUpApiSerializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "datail": "User registered successfully",
        }
        return Response(data, status=status.HTTP_201_CREATED)


class CudtomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
class GetMeApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = {
            "id" : user.id,
            "email" : user.email,
            "type" : user.user_type,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    
class GetUserApi(GenericAPIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = {
            "id" : user.id,
            "email" : user.email,
            "type" : user.user_type,
        }
        return Response(data, status=status.HTTP_200_OK)