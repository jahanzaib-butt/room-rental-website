from django.shortcuts import render, redirect, get_object_or_404
from .forms import RoomForm, RegistrationForm, RoomImage  # Ensure correct imports
from .models import Room, CATAGORY, Message, Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from templates import *
from django.http import HttpResponseForbidden 


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
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user  # Set the logged-in user as the room owner
            room.save()
            
            # Handle multiple image uploads
            images = request.FILES.getlist('images')
            for image in images:
                RoomImage.objects.create(room=room, image=image)
                
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
    if request.user != room.owner:  # Check if the logged-in user is the owner
        return HttpResponseForbidden("You are not allowed to delete this room.")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room':room}
    return render(request,'base/room_delete.html',context)

@login_required
def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)  # Ensure request.FILES is included
        if form.is_valid():
            form.save()  # Save the updated room
            
            # Handle multiple image uploads
            images = request.FILES.getlist('images')
            for image in images:
                RoomImage.objects.create(room=room, image=image)
                
            return redirect('room', pk=room.id)  # Redirect to the room detail page
        else:
            print(form.errors)  # Debugging: print form errors to console
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

@login_required(login_url='login')
def profile(request, user_id):
    profile, created = Profile.objects.get_or_create(user_id=user_id)  # Create if not exists
    rooms = Room.objects.filter(owner_id=user_id)  # Fetch rooms owned by the user
    
    if request.method == 'POST':
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('profile', user_id=user_id)

    context = {
        'profile': profile,
        'rooms': rooms  # Add rooms to the context
    }
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def edit_profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)  # Get the profile for the user

    if request.method == 'POST':
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('profile', user_id=user_id)

    context = {
        'profile': profile
    }
    return render(request, 'base/edit_profile.html', context)

@login_required  # Ensure the user is logged in
def send_message(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        message_text = request.POST['message']
        Message.objects.create(room=room, user=request.user, text=message_text)  # Save the user object
        return redirect('room_detail', room_id=room.id)  # Redirect to the room detail page

def room_detail(request, pk):  # Change 'room_id' to 'pk'
    room = get_object_or_404(Room, id=pk)  # Use 'pk' here
    context = {
        'room': room,
    }
    return render(request, 'base/room.html', context)  # Ensure this matches your template path