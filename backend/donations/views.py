from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DonationForm
from .models import Donation
from campaigns.models import Campaign
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required
def donate(request, campaign_id):
    if request.user.role != 'donor':
        return redirect('dashboard')

    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.campaign = campaign
            donation.save()

            # 🔥 Update raised amount
            campaign.raised_amount += donation.amount
            campaign.save()

            return redirect('dashboard')
    else:
        form = DonationForm()

    return render(request, 'donate.html', {'form': form, 'campaign': campaign})

@api_view(['POST'])
def donate_api(request):
    user = request.user

    if not user.is_authenticated:
        return Response({"error": "Login required"}, status=401)

    campaign_id = request.data.get("campaign_id")
    amount = request.data.get("amount")

    campaign = get_object_or_404(Campaign, id=campaign_id)

    donation = Donation.objects.create(
        donor=user,
        campaign=campaign,
        amount=amount
    )

    campaign.raised_amount += int(amount)
    campaign.save()

    return Response({"message": "Donation successful"})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer

@api_view(['GET'])
def my_donations(request):
    user = request.user

    if not user.is_authenticated:
        return Response({"error": "Login required"}, status=401)

    donations = Donation.objects.filter(donor=user)
    serializer = DonationSerializer(donations, many=True)

    return Response(serializer.data)

