from django.shortcuts import render
from .models import Room


# rooms = [
#     {'id':1, 'name':'Hello'},
#     {'id':2, 'name':'Lets learn Django'},
#     {'id':3, 'name':'Its going to be fun'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)