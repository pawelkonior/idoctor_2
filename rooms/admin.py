from django.contrib import admin


from rooms.models import Room, Availability

admin.site.register(Room)
admin.site.register(Availability)
