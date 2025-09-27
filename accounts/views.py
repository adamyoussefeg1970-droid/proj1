from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# --------------------
# Custom Views based on your images
# --------------------

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/home.html'


class RegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return HttpResponse("Error in password. Passwords do not match.")

        try:
            user = User.objects.create_user(username=username, password=password)
            return redirect('login')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('register')