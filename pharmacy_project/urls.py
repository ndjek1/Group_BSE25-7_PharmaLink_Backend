from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.pharmacies.views import PharmacyViewSet, MedicineViewSet

router = DefaultRouter()
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'medicines', MedicineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('apps.users.urls')),
]
