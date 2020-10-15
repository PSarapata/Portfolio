from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from django.urls import reverse_lazy
import django.views.generic as dv


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

