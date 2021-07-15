from django.shortcuts import render

from rooms.models import Room


def rooms_view(request):
    rooms = Room.objects.prefetch_related('availability_set')
    return render(request, 'rooms/rooms.html', {"rooms": rooms})
