from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

from campaigns.models import Campaign


class Donation(models.Model):
    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("pending", "Pending"),
        ("failed", "Failed"),
    )

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="completed")
    payment_reference = models.CharField(max_length=64, blank=True, default="")
    donated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-donated_at",)

    def __str__(self):
        return f"{self.donor} - {self.amount}"
