from rest_framework import serializers

from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    ngo_name = serializers.CharField(source="ngo.name")
    ngo_logo_url = serializers.CharField(source="ngo.logo_url", read_only=True)

    class Meta:
        model = Campaign
        fields = [
            "id",
            "title",
            "description",
            "goal_amount",
            "raised_amount",
            "category",
            "image_url",
            "location",
            "target_date",
            "ngo_name",
            "ngo_logo_url",
        ]
