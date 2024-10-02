from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create_room/', views.create_room, name='create_room'),
    path('room/<int:pk>/', views.room, name='room'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete/<str:pk>/', views.room_delete, name='room_delete'),
    path('edit/<str:pk>/', views.room_edit, name='room_edit'),
]
