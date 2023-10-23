from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Animal


# Create your views here.
class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'welcome.html')


class AnimalsView(View):
    def get(self, request, *args, **kwargs):
        query = Animal.objects.all().prefetch_related('images')
        return render(request, 'animals.html', {'animal_list': query})


class AnimalView(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Animal.objects.prefetch_related('images'), id=id)
        return render(request, 'animal.html', {'animal': query})


class SignUpView(View):

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
