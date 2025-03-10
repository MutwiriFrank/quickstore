from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "user_name", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        """
        Check if the email already exists in the database.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        """
        Validate that the two passwords match.
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        """
        Create and return a new user instance.
        """
        # Remove password2 from validated_data
        validated_data.pop("password2")

        # Create the user using the CustomAccountManager
        user = User.objects.create_user(
            email=validated_data["email"],
            user_name=validated_data["user_name"],
            password=validated_data["password"],
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["user_id"] = user.user_id
        token["email"] = user.email
        token["user_name"] = user.user_name

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        data["user_id"] = self.user.user_id
        data["email"] = self.user.email
        data["user_name"] = self.user.user_name

        return data
