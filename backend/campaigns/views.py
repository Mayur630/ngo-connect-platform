from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm
from .models import Campaign
from ngos.models import NGOProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CampaignSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from donations.models import Donation
from ngos.models import NGOProfile

@api_view(['GET'])
def stats_api(request):
    return Response({
        "total_campaigns": Campaign.objects.count(),
        "total_donations": Donation.objects.count(),
        "total_ngos": NGOProfile.objects.count(),
    })
@api_view(['GET'])
def campaign_api(request):
    campaigns = Campaign.objects.filter(is_active=True)
    serializer = CampaignSerializer(campaigns, many=True)
    return Response(serializer.data)

@login_required
def create_campaign(request):
    if request.user.role != 'ngo':
        return redirect('dashboard')

    ngo = NGOProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.ngo = ngo
            campaign.save()
            return redirect('dashboard')
    else:
        form = CampaignForm()

    return render(request, 'create_campaign.html', {'form': form})

from .models import Campaign

def campaign_list(request):
    campaigns = Campaign.objects.filter(is_active=True)
    return render(request, 'campaign_list.html', {'campaigns': campaigns})

from django.db.models import Q

def campaign_list(request):
    campaigns = Campaign.objects.filter(is_active=True)

    search_query = request.GET.get('search')
    category = request.GET.get('category')

    if search_query:
        campaigns = campaigns.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ngo__name__icontains=search_query)
        )

    if category:
        campaigns = campaigns.filter(category__icontains=category)

    return render(request, 'campaign_list.html', {'campaigns': campaigns})






