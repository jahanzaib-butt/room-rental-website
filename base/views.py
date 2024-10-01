from django.shortcuts import render, redirect
from .forms import RoomForm, RegistrationForm
from .models import Room, CATAGORY
from django.db.models import Q
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from .models import Room, CATAGORY
from django.db.models import Q

# Home page with room filtering and categories
def home(request):
    rooms = Room.objects.select_related('owner').all()
    q = request.GET.get('q') if request.GET.get('q') else ''
    
    rooms = Room.objects.filter(
        Q(catagory__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )
    
    room_count = rooms.count()
    categories = Room.objects.values_list('catagory', flat=True).distinct()
    context = {
        'rooms':rooms,
        'rooms': rooms, 
        'room_count': room_count,
        'categories': categories
        }
    print(rooms)
    return render(request, 'base/home.html', context)

# Create room view restricted to authenticated users
@login_required(login_url='login')  # Ensures only logged-in users can create rooms
def create_room(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        beds = request.POST.get('beds')
        baths = request.POST.get('baths')
        category = request.POST.get('category')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        area = request.POST.get('area')
        address = request.POST.get('address')
        
        # Automatically set the logged-in user as the owner (host)
        room = Room.objects.create(
            title=title,
            description=description,
            price=price,
            beds=beds,
            baths=baths,
            catagory=category,
            phone=phone,
            city=city,
            area=area,
            address=address,
            owner=request.user  # Set the logged-in user as the room owner
        )
        room.save()
        return redirect('home')
    
    context = {'categories': CATAGORY}
    print(f"Creating room for user: {request.user}")
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
