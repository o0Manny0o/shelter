from django.contrib import admin
from django.urls import path

from cms import views

app_name = 'cms'

urlpatterns = [
    path('<slug:page_slug>/', views.PageView.as_view(), name='page')
]
