from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django_tenants.utils import schema_context

from main.forms import SignupForm
from main.models import Client, Domain


def view_404(request, exception=None):
    return redirect('main:home')


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


class SignUp(View):
    @staticmethod
    def get(request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'sign_up.html', {'form': form})

    @staticmethod
    def post(request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            tenant = Client(schema_name=form.cleaned_data['domain'],
                            name=form.cleaned_data['username'])
            tenant.save()
            domain = Domain()
            domain.domain = form.cleaned_data['domain'] + '.localhost'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            with schema_context(tenant.schema_name):
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password1'])
                user.is_active = True
                user.is_superuser = True
                user.is_staff = True
                user.save()
            return redirect(f'http://{domain.domain}:8000/')
        else:
            return render(request, 'sign_up.html', {'form': form})

class Logout(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main:home')
        logout(request)
        return redirect('main:home')