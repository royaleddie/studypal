from django.shortcuts import render


# Create your views here.

from .models import Room

rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Lets learn Django'},
    {'id':3, 'name':'Lets learn Together'},
]

def home(request):
    rooms = rooms.object.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)
