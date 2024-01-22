from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Log in the user after successful registration
        return response
    
class EditAccountView(LoginRequiredMixin, View):
    template_name = 'edit_account.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')  # Change 'profile' to your profile URL name

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated successfully.')
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    user = request.user
    context ={
        'user': user
    }
    return render(request, 'profile.html', context)
