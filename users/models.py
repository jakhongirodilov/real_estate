from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    balance = models.FloatField(default=1000.0)

