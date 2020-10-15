from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('room/new/', views.CreateRoomView.as_view(), name='create room'),
    path('rooms/', views.RoomListView.as_view(), name='list view'),
    re_path(r'^room/delete/(?P<pk>[1-9]+)/$', views.RoomDeleteView.as_view(), name='delete view'),
    re_path(r'^room/modify/(?P<pk>[1-9]+)/$', views.RoomModifyView.as_view(), name='modify view'),
]
