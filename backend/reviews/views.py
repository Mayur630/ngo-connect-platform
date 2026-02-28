from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from ngos.models import NGOProfile

@login_required
def add_review(request, ngo_id):
    if request.user.role != 'donor':
        return redirect('dashboard')

    ngo = get_object_or_404(NGOProfile, id=ngo_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.donor = request.user
            review.ngo = ngo
            review.save()
            return redirect('campaign_list')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'ngo': ngo})