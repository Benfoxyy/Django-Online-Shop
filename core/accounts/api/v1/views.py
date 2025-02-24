from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer,CustomTokenRefreshSerializer,GetUserApiSerializers
from .serializers import SignUpApiSerializers
from accounts.models import User, Profile


class SignUpApiView(generics.GenericAPIView):
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
    
class GetMeApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserApiSerializers
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    
    
class GetUserApiView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GetUserApiSerializers
    queryset = Profile.objects.all()