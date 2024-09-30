from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create_room/', views.create_room, name='create_room'),
    path('room/<str:pk>/', views.room, name='room'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/',views.logout_page, name='logout'),

    # Add more URL patterns as needed
]