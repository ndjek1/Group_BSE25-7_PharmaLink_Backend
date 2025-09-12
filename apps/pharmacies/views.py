# apps/pharmacies/views.py

from rest_framework import viewsets, permissions
# We don't need these for the secure version
# from rest_framework.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from .models import Pharmacy, Medicine
from .serializers import PharmacySerializer, MedicineSerializer
from django.shortcuts import render


# User = get_user_model() # No longer needed here

class PharmacyViewSet(viewsets.ModelViewSet):
    """
    This ViewSet is open for anyone to view pharmacies.
    """
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicineViewSet(viewsets.ModelViewSet):
    """
    Anyone can view medicines.
    Only authenticated users can add/update/delete.
    """
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def index(request):
    return render(request, "index.html")
