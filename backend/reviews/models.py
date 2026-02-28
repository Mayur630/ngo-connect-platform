from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings

from ngos.models import NGOProfile


class Review(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ngo = models.ForeignKey(NGOProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.ngo} - {self.rating}"
