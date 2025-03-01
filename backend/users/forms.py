from django.contrib.auth import forms
from users.models import CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "bio"]

