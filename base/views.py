from django.shortcuts import render

rooms = [
    {"id": 1, "name": "Let's all learn python!"},
    {"id": 2, "name": "Are you a designer"},
    {"id": 3, "name": "Frontend developer"},
]

def Home(request):
    """ Home page """
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def Room(request):
    """ The room page """
    return render(request, "base/room.html")