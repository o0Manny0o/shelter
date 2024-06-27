from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Animal


# Create your views here.
class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'welcome.html')


class AnimalsView(View):
    def get(self, request, *args, **kwargs):
        animals = cache.get("animals")
        if animals is None:
            animals = Animal.objects.all().prefetch_related('images')
            cache.set("animals", list(animals), 10 * 60)
        return render(request, 'animals.html', {'animal_list': animals})


class AnimalView(View):
    def get(self, request, id, *args, **kwargs):
        animal = cache.get(f"animal_{id}")
        if animal is None:
            animal = get_object_or_404(Animal.objects.prefetch_related('images'), id=id)
            cache.set(f"animal_{id}", animal, 10 * 60)
        return render(request, 'animal.html', {'animal': animal})


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
