from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("ngo", "donor", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("ngo__name", "donor__username", "comment")
    date_hierarchy = "created_at"
    autocomplete_fields = ("donor", "ngo")
