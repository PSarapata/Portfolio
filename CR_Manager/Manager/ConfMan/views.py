from django.shortcuts import render, redirect
from .models import Room, Reservation
from django.urls import reverse_lazy
import django.views.generic as dv
import datetime


class HomeView(dv.TemplateView):
    template_name = 'ConfMan/html/index.html'


class CreateRoomView(dv.CreateView):
    model = Room
    fields = ['name', 'capacity', 'has_projector']
    template_name = 'ConfMan/html/room_create_form.html'


class RoomListView(dv.View):
    def get(self, request):
        template_name = 'ConfMan/html/room_list.html'
        queryset = Room.objects.all()
        for room in queryset:
            reservations = [reservation.date for reservation in room.reservation_set.all()]
            room.unavailable = datetime.date.today() in reservations
        return render(request, template_name, context={'room_list': queryset})


class RoomDeleteView(dv.DeleteView):
    model = Room
    template_name = 'ConfMan/html/confirm_delete.html'
    success_url = reverse_lazy('list view')


class RoomModifyView(dv.UpdateView):
    model = Room
    fields = [
        'name',
        'capacity',
        'has_projector'
    ]
    template_name = 'ConfMan/html/room_modify.html'
    success_url = reverse_lazy('list view')


class RoomReservationView(dv.View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, 'ConfMan/html/room_reserve.html', context={'room': room})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        date = request.POST['date']
        comment = request.POST['comment']
        if Reservation.objects.filter(room_id=room, date=date):
            return render(request, 'ConfMan/html/room_reserve.html', context={"room": room,
                                                                              "error": "Room has been taken!"})
        if date < str(datetime.date.today()):
            return render(request, 'ConfMan/html/room_reserve.html', context={"room": room,
                                                                              "error": "Reservation is in the past!"})
        Reservation.objects.create(date=date, room_id=room, comment=comment)
        return redirect('/rooms/')


class RoomDetailView(dv.DetailView):
    model = Room
    template_name = 'ConfMan/html/room_detail_view.html'


class RoomSearchView(dv.View):
    def get(self, request):

        name = request.GET.get("name")

        capacity = request.GET.get("capacity")

        capacity = int(capacity) if capacity else 0

        has_projector = request.GET.get("projector") == 'on'

        rooms = Room.objects.all()

        if has_projector:
            rooms = rooms.filter(has_projector=has_projector)

        if capacity:
            rooms = rooms.filter(capacity__gte=capacity)

        if name:
            rooms.filter(name__icontains=name)

        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.reservation_set.all()]

            room.reserved = str(datetime.date.today()) in reservation_dates

        return render(
            request,
            "ConfMan/html/search_form.html",
            context={
                "rooms": rooms,
                "form": {'name': name, 'capacity': capacity, 'has_projector': has_projector}
            }
        )
