from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
#        path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
  path("login/", views.login, name="login"),
  path("logout/", views.logout, name="logout"),
  path("signup/", views.signup, name="signup"),
  path("list-users/", views.list_users, name="list-users"),
  path("password-change/", auth_views.PasswordChangeView.as_view(), name="password-change"),
  path("password-change-done/", auth_views.PasswordChangeDoneView.as_view(), name="password-change-done"),
  path("password-reset/", auth_views.PasswordResetView.as_view(), name="password-reset"),
  path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password-reset-done"),
  path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
  path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password-reset-complete"),
]
