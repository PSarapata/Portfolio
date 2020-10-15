from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('room/new/', views.CreateRoomView.as_view(), name='create room'),
    path('rooms/', views.RoomListView.as_view(), name='list views'),
]
