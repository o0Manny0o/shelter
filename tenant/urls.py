from django.urls import path, include

from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('auth/sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('', views.TestView.as_view(), name='welcome'),
    path('animals', views.AnimalsView.as_view(), name='animals'),
    path('animal/<int:id>', views.AnimalView.as_view(), name='animal'),
    path('', include('cms.urls')),
]
