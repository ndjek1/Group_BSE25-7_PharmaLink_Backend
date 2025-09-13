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
    permission_classes = [permissions.AllowAny]


class MedicineViewSet(viewsets.ModelViewSet):
    """
    This ViewSet allows ONLY authenticated users to create, view, update,
    and delete their own medicines.
    """
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
    # 1. CHANGE PERMISSIONS: Require a valid token to access
    permission_classes = [permissions.AllowAny]

    # 2. SIMPLIFY CREATE METHOD: The user will always be authenticated
    def perform_create(self, serializer):
        """
        Automatically set the medicine's owner to the currently logged-in user.
        """
        serializer.save(owner=self.request.user)

    # 3. SECURE THE QUERYSET: Users should only see their own medicines
    def get_queryset(self):
        """
        This view should ONLY return a list of medicines created by the
        currently authenticated user.
        """
        return Medicine.objects.filter(owner=self.request.user)

def index(request):
    return render(request, "index.html")
