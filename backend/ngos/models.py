from django.conf import settings
from django.db import models


DEFAULT_NGO_LOGO_URL = (
    "https://images.unsplash.com/photo-1469571486292-b53601020d26?auto=format&fit=crop&w=400&q=80"
)
DEFAULT_NGO_COVER_URL = (
    "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1400&q=80"
)


class NGOProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    website = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, default=DEFAULT_NGO_LOGO_URL)
    cover_image_url = models.URLField(blank=True, default=DEFAULT_NGO_COVER_URL)
    city = models.CharField(max_length=120, blank=True, default="")
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-verified", "name")

    def __str__(self):
        return self.name
