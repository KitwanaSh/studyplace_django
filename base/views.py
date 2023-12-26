from django.shortcuts import render
from .models import Room

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