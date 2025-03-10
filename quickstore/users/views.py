from rest_framework import viewsets, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .serializers import CustomTokenObtainPairSerializer, UserRegistrationSerializer


class AuthViewSet(viewsets.ViewSet):
    """
    ViewSet for handling authentication-related actions (e.g., registration,
    token generation and logout).
    """

    @extend_schema(
        request=UserRegistrationSerializer,
        responses={
            201: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "Example Request",
                value={
                    "email": "user@example.com",
                    "user_name": "user123",
                    "password": "yourpassword",
                    "password2": "yourpassword",
                },
                request_only=True,  # Only for request body
            ),
        ],
    )
    @action(detail=False, methods=["post"])
    def register(self, request):
        """
        Custom action for user registration.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=CustomTokenObtainPairSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "Example Request",
                value={
                    "email": "user@example.com",
                    "password": "yourpassword",
                },
                request_only=True,  # Only for request body
            ),
        ],
    )
    @action(detail=False, methods=["post"])
    def login(self, request):
        """
        Generates JWT tokens for the user.
        """
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @extend_schema(
        request=OpenApiTypes.OBJECT,
        responses={
            205: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "Example Request",
                value={
                    "refresh": "your-refresh-token",
                },
                request_only=True,  # Only for request body
            ),
        ],
    )
    @action(detail=False, methods=["post"])
    def logout(self, request):
        """
        Logs out the user by blacklisting the refresh token.
        """
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(
                {"error": "Invalid token or token not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )
