from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Reservation
from django.urls import reverse_lazy
import django.views.generic as dv
import datetime


class HomeView(dv.View):
    def get(self, request):
        return render(request, 'ConfMan/html/index.html')


class CreateRoomView(dv.CreateView):
    model = Room
    fields = ['name', 'capacity', 'has_projector']
    template_name = 'ConfMan/html/room_create_form.html'


class RoomListView(dv.ListView):
    model = Room
    template_name = 'ConfMan/html/room_list.html'
    queryset = Room.objects.all()
    context_object_name = 'room_list'


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


class RoomReservationView(dv.UpdateView):
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
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        reservations = Reservation.objects.filter(room_id=room_id)
        return render(request, 'ConfMan/html/room_detail_view.html', context={'room': room, 'reservations': reservations})
