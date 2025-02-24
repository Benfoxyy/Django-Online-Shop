from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from accounts.models import User, Profile


class SignUpApiSerializers(serializers.ModelSerializer):
    password_conf = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password_conf"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password_conf"):
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password_conf")
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["id"] = self.user.id
        validated_data["email"] = self.user.email
        return validated_data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["id"] = self.user.id
        validated_data["email"] = self.user.email
        return validated_data
    
class GetUserApiSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    id = serializers.IntegerField(source="user.id", read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "email", "first_name", "last_name", "phone_number", "avatar", "created_date"]