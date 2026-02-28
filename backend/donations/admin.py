from django.contrib import admin

from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor", "campaign", "amount", "status", "payment_reference", "donated_at")
    search_fields = ("donor__username", "campaign__title", "payment_reference")
    list_filter = ("status", "donated_at")
    date_hierarchy = "donated_at"
    autocomplete_fields = ("donor", "campaign")
