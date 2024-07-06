# freelancing/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserProfileForm, WorkRequestForm
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_edit')
    else:
        form = UserRegistrationForm()
    return render(request, 'freelancing/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_edit')
    else:
        form = AuthenticationForm()
    return render(request, 'freelancing/login.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'freelancing/profile_edit.html', {'form': form})

@login_required
def work_request_submit(request):
    if request.method == 'POST':
        form = WorkRequestForm(request.POST)
        if form.is_valid():
            work_request = form.save(commit=False)
            work_request.client = request.user
            work_request.save()
            return redirect('work_request_submit')
    else:
        form = WorkRequestForm()
    return render(request, 'freelancing/work_request_submit.html', {'form': form})
