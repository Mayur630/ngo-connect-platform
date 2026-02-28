from django.contrib import admin
from django.utils.html import format_html

from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "banner_preview",
        "title",
        "ngo",
        "category",
        "goal_amount",
        "raised_amount",
        "progress_value",
        "is_active",
        "target_date",
        "created_at",
    )
    search_fields = ("title", "ngo__name", "category", "location")
    list_filter = ("is_active", "category", "location", "created_at", "target_date")
    list_editable = ("is_active",)
    date_hierarchy = "created_at"
    autocomplete_fields = ("ngo",)
    readonly_fields = ("banner_preview", "progress_value", "created_at")

    fieldsets = (
        ("Campaign Basics", {"fields": ("ngo", "title", "description", "category", "location")}),
        ("Campaign Media", {"fields": ("image_url", "banner_preview")}),
        (
            "Funding",
            {
                "fields": (
                    "goal_amount",
                    "raised_amount",
                    "progress_value",
                )
            },
        ),
        ("Timeline & Status", {"fields": ("target_date", "is_active", "created_at")}),
    )

    def banner_preview(self, obj):
        return format_html(
            '<img src="{}" alt="{}" style="width:86px;height:50px;border-radius:8px;object-fit:cover;"/>',
            obj.image_url,
            obj.title,
        )

    banner_preview.short_description = "Image"

    def progress_value(self, obj):
        return f"{obj.progress_percent}%"

    progress_value.short_description = "Funded"
