from django.urls import path
from .views import MedicineViewSet, PharmacyViewSet

# --- Manual URL configuration for Medicines ---

# URL for listing all medicines and creating a new one
medicine_list = MedicineViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# URL for retrieving, updating, or deleting a single medicine
medicine_detail = MedicineViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# --- Manual URL configuration for Pharmacies ---

pharmacy_list = PharmacyViewSet.as_view({'get': 'list', 'post': 'create'})
pharmacy_detail = PharmacyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})


urlpatterns = [
    path('medicines/', medicine_list, name='medicine-list'),
    path('medicines/<int:pk>/', medicine_detail, name='medicine-detail'),
    
    path('pharmacies/', pharmacy_list, name='pharmacy-list'),
    path('pharmacies/<int:pk>/', pharmacy_detail, name='pharmacy-detail'),
]