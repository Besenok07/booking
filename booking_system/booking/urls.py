from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('rooms/', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('availabilities/', views.availability_list, name='availability_list'),
]