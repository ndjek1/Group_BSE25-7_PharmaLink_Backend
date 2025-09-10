# your_app/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pharmacy(models.Model):
    # Your pharmacy fields...
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pharmacy = models.ForeignKey(Pharmacy, related_name='medicines', on_delete=models.CASCADE)
    
    # --- ADD THIS FIELD ---
    # This links each medicine to a user.
    # on_delete=models.CASCADE means if a user is deleted, their medicines are also deleted.
    owner = models.ForeignKey(User, related_name='medicines', on_delete=models.CASCADE)

    def __str__(self):
        return self.name