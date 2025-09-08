from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_pharmacist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
