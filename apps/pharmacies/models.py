from django.db import models
from apps.users.models import User

class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="medicines")

    def __str__(self):
        return f"{self.name} ({self.pharmacy.name})"
