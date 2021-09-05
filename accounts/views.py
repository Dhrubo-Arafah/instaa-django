from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import CreateNewUser, EditProfile, EditUser
from accounts.models import UserProfile


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            userprofile = UserProfile(user=user)
            UserProfile.objects.create(user=user)
            return HttpResponseRedirect(reverse('login'))
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    user_form = EditUser(instance=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        user_form = EditUser(request.POST, instance=request.user)
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return HttpResponseRedirect(reverse('profile'))
    context = {
        'user_form':user_form,
        'form': form
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def profile(request):
    context = {}
    return render(request, 'accounts/user.html', context)
