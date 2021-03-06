from email.mime import message
from hashlib import new
from os import name
import re
from django.shortcuts import redirect, render
from chat.models import Room, Messages
from django.http import HttpResponse , JsonResponse

# Create your views here.


def home(request):
    return render(request , 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST.get('room_name')
    username= request.POST.get('username')
  
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
          

def send(request):
    message = request.POST.get('message')
    room_id = request.POST.get('room_id')
    username = request.POST.get('username')

    new_message = Messages.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent succesfully')

def getMessages(request,room):
    room_details = Room.objects.get(name=room)

    messages = Messages.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})