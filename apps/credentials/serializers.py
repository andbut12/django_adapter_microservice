from rest_framework import serializers


class SignInRequestSerializer(serializers.Serializer):
    username: str = serializers.CharField(max_length=32, default="user")
    password: str = serializers.CharField(max_length=128, default="password")


class SignInResponseSerializer(serializers.Serializer):
    id: int = serializers.IntegerField()
    token: str = serializers.CharField()
