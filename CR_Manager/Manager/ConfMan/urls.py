from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('room/new/', views.CreateRoomView.as_view(), name='create room'),
    path('rooms/', views.RoomListView.as_view(), name='list view'),
    path('search/', views.RoomSearchView.as_view(), name='search view'),
    re_path(r'^room/delete/(?P<pk>[1-9]+)/$', views.RoomDeleteView.as_view(), name='delete view'),
    re_path(r'^room/modify/(?P<pk>[1-9]+)/$', views.RoomModifyView.as_view(), name='modify view'),
    re_path(r'^room/reserve/(?P<room_id>[1-9]+)/$', views.RoomReservationView.as_view(), name='reservation view'),
    re_path(r'^room/detail/(?P<room_id>[1-9]+)/$', views.RoomDetailView.as_view(), name='detail view'),
]
