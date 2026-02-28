from django.contrib import admin
from django.urls import path

from accounts.views import register_view, dashboard
from django.contrib.auth import views as auth_views
from campaigns.views import create_campaign, campaign_list
from reviews.views import add_review
from campaigns.views import campaign_api
from accounts.views import login_api, register_api
from donations.views import donate_api
from donations.views import my_donations
from campaigns.views import stats_api


admin.site.site_header = "NGO Connect Administration"
admin.site.site_title = "NGO Connect Admin"
admin.site.index_title = "Platform Control Panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create-campaign/', create_campaign, name='create_campaign'),
    path('campaigns/', campaign_list, name='campaign_list'),
    path('review/<int:ngo_id>/', add_review, name='add_review'),
    path('api/campaigns/', campaign_api),
    path('api/login/', login_api),
    path('api/register/', register_api),
    path('api/donate/', donate_api),
    path('api/my-donations/', my_donations),
    path('api/stats/', stats_api),
]
