from django.db import models

# Create your models here.
from django.db import models
from ngos.models import NGOProfile

class ServiceRequest(models.Model):
    ngo = models.ForeignKey(NGOProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Open")

    def __str__(self):
        return self.title