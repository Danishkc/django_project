from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserProfileForm, UserRegistrationForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('profile_update')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile_update(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_update')
    else:
        user_form = UserRegistrationForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'profiles/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})
