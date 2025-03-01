from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
        path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
   path("signup/", views.signup, name="signup"),
   path("password-change/", auth_views.PasswordChangeView.as_view(), name="password-change"),
   path("password-change-done/", auth_views.PasswordChangeDoneView.as_view(), name="password-change-done"),
   path("password-reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password-reset"),
   path("list-users/", views.list_users, name="list-users"),
]

