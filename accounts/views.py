from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')

    return render(request, 'register.html')


# LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)  # session created
            return redirect('home')

    return render(request, 'login.html')


# HOME (Protected)
@login_required
def home(request):
    return render(request, 'home.html')


# LOGOUT
def user_logout(request):
    logout(request)  # session destroyed
    return redirect('login')