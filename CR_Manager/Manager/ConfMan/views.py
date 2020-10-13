from django.http import HttpResponse
from django.shortcuts import render, redirect
import django.views.generic as dv


class HomeView(dv.View):
    def get(self, request):
        return render(request, 'ConfMan/html/index.html')
