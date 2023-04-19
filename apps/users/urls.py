from django.urls import path

from .api_endpoints import auth

app_name = "users"

urlpatterns = [
    path("login/", auth.LoginView.as_view(), name="auth-login"),
    path("create/", auth.RegisterView.as_view(), name="auth-create"),
]
