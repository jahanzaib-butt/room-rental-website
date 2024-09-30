from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import *

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    room_count =  rooms.count()
    context  = {'rooms': rooms,'room_count':room_count}
    return render(request, 'base/home.html',context)

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
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





