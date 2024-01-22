from django.urls import path
from .views import SignUpView, profile, logout_view, EditAccountView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile"),
    path('edit_account/', EditAccountView.as_view(), name='edit_account'),
]