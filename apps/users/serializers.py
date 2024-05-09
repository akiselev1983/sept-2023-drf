from rest_framework import serializers

from apps.auto_parks.serializer import AutoParkSerializer, AutoParkWithCarsSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithCarsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'age', 'created_at', 'updated_at', 'auto_parks')