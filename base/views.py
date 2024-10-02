from django.shortcuts import render, redirect
from .forms import RoomForm, RegistrationForm
from .models import Room, CATAGORY
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from templates import *


# Home page with room filtering and categories
def home(request):
    q = request.GET.get('q', '')
    rooms = Room.objects.filter(
        Q(catagory__icontains=q) |
        Q(title__icontains=q) |
        Q(owner__username__icontains=q) |
        Q(description__icontains=q)
    ).select_related('owner')

    room_count = rooms.count()
    categories = Room.objects.values_list('catagory', flat=True).distinct()  # Get distinct categories

    context = {
        'rooms': rooms,
        'room_count': room_count,
        'categories': categories
    }
    return render(request, 'base/home.html', context)


# Create room view restricted to authenticated users
@login_required(login_url='login')
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user  # Set the logged-in user as the room owner
            room.save()
            return redirect('home')
    else:
        form = RoomForm()  # Create an instance of the form

    context = {'form': form}  # Pass the form to the context
    return render(request, 'base/create_room.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,  'base/room.html',context)

@login_required(login_url='Login')
def room_delete(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room':room}
    return render(request,'base/room_delete.html',context)

@login_required(login_url='login')
def room_edit(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm(instance=room)
    context = {'form': form, 'room': room}
    return render(request, 'base/room_edit.html', context)



def register(request):
    if request.method == 'POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =  RegistrationForm()
    context = {'form': form}
    return  render(request, 'base/register.html',context)

def  login_page(request):
    return render(request, 'base/login.html')


def logout_page(request):
    auth_logout(request)
    return redirect('login')

def navbar(request):
    room = Room.objects.all()
    context = {'room':room}
    return render(request,'templates/navbar.html',context)

def profile(request):
    user = Room.objects.all()
    context = {'user':user}
    return render(request,'base/profile.html',context)