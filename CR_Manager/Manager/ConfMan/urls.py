from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
]
