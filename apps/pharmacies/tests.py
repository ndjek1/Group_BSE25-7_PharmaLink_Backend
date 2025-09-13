from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Pharmacy

User = get_user_model()

class PharmacyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='pharmacy@example.com',
            password='testpass123'
        )
        
    def test_create_pharmacy(self):
        """Test creating a new pharmacy"""
        pharmacy = Pharmacy.objects.create(
            name='Test Pharmacy',
            address='123 Main St'
        )
        self.assertEqual(pharmacy.name, 'Test Pharmacy')
        self.assertEqual(pharmacy.address, '123 Main St')
        
    def test_pharmacy_str_representation(self):
        """Test pharmacy string representation"""
        pharmacy = Pharmacy.objects.create(
            name='Test Pharmacy',
            address='123 Main St'
        )
        self.assertEqual(str(pharmacy), 'Test Pharmacy')

class PharmacyAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='pharmacy@example.com',
            password='testpass123'
        )
        self.pharmacy = Pharmacy.objects.create(
            name='Test Pharmacy',
            address='123 Main St'
        )
        
    def test_pharmacy_list_api(self):
        """Test pharmacy list API endpoint"""
        response = self.client.get('/api/pharmacies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_pharmacy_detail_api(self):
        """Test pharmacy detail API endpoint"""
        response = self.client.get(f'/api/pharmacies/{self.pharmacy.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Pharmacy')
