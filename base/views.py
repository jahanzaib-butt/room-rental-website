from django.shortcuts import render, redirect
from .forms import RoomForm, RegistrationForm
from .models import *
from django.db.models import Q
from django.contrib.auth import logout as auth_logout

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    rooms = Room.objects.filter(
        Q(catagory__icontains=q) |
        Q(title__icontains=q) |
        Q(host__username__icontains=q) |
        Q(description__icontains=q)
    )
    
    room_count = rooms.count()
    categories = Room.objects.values_list('catagory', flat=True).distinct()  # Get distinct categories
    context = {'rooms': rooms, 'room_count': room_count, 'categories': categories}
    return render(request, 'base/home.html', context)

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            # Save the room directly without checking for existing categories
            room = form.save(commit=False)
            room.host = request.user
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    context = {'form': form}
    return render(request, 'base/create_room.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,  'base/room.html',context)



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
