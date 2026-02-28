
from ngos.models import NGOProfile
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({
            "message": "Login successful",
            "role": user.role,
            "username": user.username
        })
    else:
        return Response({"error": "Invalid credentials"}, status=400)
from .models import User

@api_view(['POST'])
def register_api(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        role=role
    )

    return Response({"message": "User created successfully"})
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 🔥 If user is NGO, create NGO Profile automatically
            if user.role == 'ngo':
                NGOProfile.objects.create(
                    user=user,
                    name=user.username
                )

            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user

    if user.role == 'donor':
        return render(request, 'donor_dashboard.html')

    elif user.role == 'ngo':
        return render(request, 'ngo_dashboard.html')

    elif user.role == 'volunteer':
        return render(request, 'volunteer_dashboard.html')

    else:
        return render(request, 'dashboard.html')


