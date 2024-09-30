from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_room/', views.create_room, name='create_room'),
    # Add more URL patterns as needed
]