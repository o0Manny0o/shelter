from django.urls import path

from main import views


app_name = "main"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sign-up', views.SignUp.as_view(), name='signup'),
    path('logout', views.Logout.as_view(), name='logout')
]

handler404 = 'main.views.view_404'
