# your_app/serializers.py

from rest_framework import serializers
from .models import Pharmacy, Medicine

# Assuming you have a UserSerializer like the one from our previous discussions
from django.contrib.auth import get_user_model

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    # This makes the API response more readable by showing the username
    # instead of just the user's ID.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Medicine
        # Add 'owner' to the list of fields
        fields = ['id', 'name', 'description', 'price', 'owner']