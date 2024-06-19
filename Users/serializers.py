from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import logging

logger = logging.getLogger(__name__)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
            user.save()
            return user


class TokenObtainPairSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        logger.debug(f"Validating user with email: {email}")
        user=authenticate(request=self.context.get('request'),email=email,password=password)
        if user is None:
            logger.error('Invalid credentials')
            raise serializers.ValidationError(('Invalid credentials'), code='authorization')
        refresh = RefreshToken.for_user(user)
        logger.info(f"User {email} authenticated successfully")
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'id': user.id,
            'email': user.email,
           
        }

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            refresh = RefreshToken.for_user(user)
            if user is None:
                raise serializers.ValidationError('Invalid credentials', code='authorization')

        return {
                    'user': user,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'id': user.id,
                    'email': user.email,
        }