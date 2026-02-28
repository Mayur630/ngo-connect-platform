from django.core.validators import MinValueValidator
from django.db import models

from ngos.models import NGOProfile


DEFAULT_CAMPAIGN_IMAGE_URL = (
    "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=1400&q=80"
)


class Campaign(models.Model):
    ngo = models.ForeignKey(NGOProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    raised_amount = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, default="General")
    image_url = models.URLField(blank=True, default=DEFAULT_CAMPAIGN_IMAGE_URL)
    location = models.CharField(max_length=120, blank=True, default="")
    target_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    @property
    def progress_percent(self):
        if self.goal_amount <= 0:
            return 0
        return min(100, round((self.raised_amount / self.goal_amount) * 100))

    def __str__(self):
        return self.title
