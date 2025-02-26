from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib import messages

User = get_user_model()

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = auth_forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.SUCCESS
            return redirect("users:login")
    else:
        form = auth_forms.UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def update_destroy_user(request, pk):
    pass

