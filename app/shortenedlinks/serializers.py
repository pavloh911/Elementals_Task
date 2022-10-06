from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import SLink, User


class SLinkSerializer(serializers.ModelSerializer):
    User = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SLink
        fields = ("id", "User", "link", "count")


class SLinkSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = SLink
        fields = ("id", "User", "link", "count")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
