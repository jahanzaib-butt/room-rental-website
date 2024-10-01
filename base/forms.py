from django import forms
from .models import Room
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
        fields = ['title', 'description', 'price', 'beds', 'baths', 'catagory', 'phone', 'city', 'area', 'address']
        widgets = {
            'catagory': forms.Select(choices=CATAGORY),  # Use dropdown for categories
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
