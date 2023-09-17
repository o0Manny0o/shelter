from django.urls import path, include

from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('auth/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('', views.Test.as_view(), name='welcome'),
    path('animals', views.Animals.as_view(), name='animals'),
    path('', include('cms.urls')),
]
