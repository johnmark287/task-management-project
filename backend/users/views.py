from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            messages.success(request, "Account created successfully")
            return redirect(reverse("users:login"))
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def login(request):
    if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        if user is not None:
          auth_login(request, user)
          messages.info(request, "User logged in successfully.")
          return redirect(reverse("tasks:index"))
    if request.method == "GET":
        form = AuthenticationForm()
    return render(request, "registration/login.html", { "form": form })
    
def logout(request):
  auth_logout(request)
  return redirect(reverse("users:login"))

# @login_required
def list_users(request):
    users = User.objects.all()
    return render(request, "registration/list_users.html", { "users": users })

@login_required(login_url="users/login")
def profile(request):
  print("hello")
  return render(request, {})
