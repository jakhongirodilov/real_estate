from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Log in the user after successful registration
        return response

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    user = request.user

    context ={
        'user': user
    }

    return render(request, 'profile.html', context)
