from django.shortcuts import render

from rooms.models import Room


def rooms_view(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {"rooms": rooms})
