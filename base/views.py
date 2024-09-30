from django.shortcuts import render, redirect
from .forms import RoomForm

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

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