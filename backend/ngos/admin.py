from django.contrib import admin
from django.utils.html import format_html

from .models import NGOProfile


@admin.register(NGOProfile)
class NGOAdmin(admin.ModelAdmin):
    list_display = ("logo_preview", "name", "user", "city", "verified", "website_link", "created_at")
    list_filter = ("verified", "city", "created_at")
    search_fields = ("name", "user__username", "city")
    readonly_fields = ("logo_preview", "cover_preview", "created_at")

    fieldsets = (
        ("NGO Details", {"fields": ("user", "name", "description", "city", "verified")}),
        (
            "Branding & Links",
            {"fields": ("logo_url", "logo_preview", "cover_image_url", "cover_preview", "website")},
        ),
        ("System", {"fields": ("created_at",)}),
    )

    def logo_preview(self, obj):
        return format_html(
            '<img src="{}" alt="{}" style="width:48px;height:48px;border-radius:10px;object-fit:cover;"/>',
            obj.logo_url,
            obj.name,
        )

    logo_preview.short_description = "Logo"

    def cover_preview(self, obj):
        return format_html(
            '<img src="{}" alt="{} cover" style="width:220px;height:90px;border-radius:10px;object-fit:cover;"/>',
            obj.cover_image_url,
            obj.name,
        )

    cover_preview.short_description = "Cover Preview"

    def website_link(self, obj):
        if not obj.website:
            return "-"
        return format_html('<a href="{}" target="_blank" rel="noopener noreferrer">Visit</a>', obj.website)

    website_link.short_description = "Website"
