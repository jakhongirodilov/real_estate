from django.urls import path
from .views import SignUpView, profile, logout_view

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile")
]