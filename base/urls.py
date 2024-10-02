from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import send_message, room_detail  # Ensure you import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create_room/', views.create_room, name='create_room'),
    path('room/<int:pk>/', views.room_detail, name='room'),  # Ensure this matches
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/edit/<int:user_id>/', views.edit_profile, name='edit_profile'),  # Add this line
    path('delete/<str:pk>/', views.room_delete, name='room_delete'),
    path('edit/<str:pk>/', views.room_edit, name='room_edit'),
    path('room/<int:room_id>/send_message/', send_message, name='send_message'),  # Send message view
]
