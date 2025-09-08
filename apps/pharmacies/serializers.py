from rest_framework import serializers
from .models import Pharmacy, Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    medicines = MedicineSerializer(many=True, read_only=True)

    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'address', 'medicines']
