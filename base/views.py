from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    """ Home page """
    return HttpResponse("Home Page")

def Room(request):
    """ The room page """
    return HttpResponse("The room page!")