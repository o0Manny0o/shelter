from django.contrib import admin
from django.urls import path

from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('auth/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('', views.Test.as_view(), name='welcome'),
]
