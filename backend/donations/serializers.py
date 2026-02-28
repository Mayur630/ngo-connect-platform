from rest_framework import serializers

from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    campaign_title = serializers.CharField(source='campaign.title')

    class Meta:
        model = Donation
        fields = ['id', 'campaign_title', 'amount', 'status', 'payment_reference', 'donated_at']
