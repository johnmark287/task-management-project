from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth import forms as auth_forms
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
#from django.urls import reverse
User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully")
            return redirect("users:login")
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm()
        if form.is_valid():
            form.save()
            return redirect("tasks:list-tasks")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", { "form": form })

def list_users(request):
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request, "registration/list_users.html", { "users": users })

