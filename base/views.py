from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {"id": 1, "name": "Let's all learn python!"},
#     {"id": 2, "name": "Are you a designer"},
#     {"id": 3, "name": "Frontend developer"},
# ]

def home(request):
    """ Home page """
    rooms = Room.objects.all()
    context = {'rooms': rooms}

    return render(request, "base/home.html", context)

def room(request, pk):
    """ The room page """
    room = Room.objects.get(id=pk)
    context = {'room': room}
    
    return render(request, "base/room.html", context)

def createRoom(request):
    """ Views for the create room form """
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request, "base/room_form.html", context)