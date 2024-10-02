from django import forms
from .models import Room, RoomImage  # Ensure only Room and RoomImage are imported here
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CATAGORY = (
    ('Home', 'Home'),
    ('Apartment', 'Apartment'),
    ('ROOMS', 'ROOMS'),
    ('Office', 'Office'),
    ('Farmhouse', 'Farmhouse')
)

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'price', 'beds', 'baths', 'catagory', 'phone', 'city', 'area', 'address', 'image']  # Ensure 'image' is included
        widgets = {
            'catagory': forms.Select(choices=CATAGORY),  # Use dropdown for categories
        }

class RegistrationForm(forms.ModelForm):
    # Define your fields and Meta class here
    class Meta:
        model = User  # Replace with your actual user model
        fields = ['username', 'email', 'password']  # Adjust fields as necessary

class RoomImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = ['image']
