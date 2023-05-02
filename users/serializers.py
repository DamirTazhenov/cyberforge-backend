from rest_framework import serializers

from configurator.serializers import ModificationSerializer, ModificationGetSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    modifications = ModificationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password', 'modifications')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['modifications']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user

