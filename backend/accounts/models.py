from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("donor", "Donor"),
        ("ngo", "NGO"),
        ("volunteer", "Volunteer"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="donor")
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
