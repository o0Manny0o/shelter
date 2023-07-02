from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Test(View):
    def get(self, request, *args, **kwargs):
        print(request.tenant)
        return render(request, 'welcome.html')


class SignUp(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('tenant:welcome')
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('tenant:welcome')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tenant:welcome")
        else:
            return render(request, 'registration/register.html', {'form': form})
