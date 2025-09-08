from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_pharmacist', 'is_patient']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_pharmacist=validated_data.get('is_pharmacist', False),
            is_patient=validated_data.get('is_patient', True),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
