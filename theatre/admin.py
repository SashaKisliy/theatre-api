from django.contrib import admin

from .models import (
    TheatreHall,
    Genre,
    Actor,
    Play,
    Performance,
    Ticket,
    Reservation
)

admin.site.register(TheatreHall)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(Performance)
admin.site.register(Ticket)
admin.site.register(Reservation)
