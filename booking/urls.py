from django.urls import path
from .views import book_appointment, get_available_time_slots, user_info, edit_booking, delete_booking

urlpatterns = [
    path('booking/<int:booking_id>/edit/', edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('get_available_time_slots/', get_available_time_slots, name='get_available_time_slots'),
    path('user_info/', user_info, name='user_info'),
    path('', book_appointment, name='book_appointment'),
    path('book/<int:massage_id>/', book_appointment, name='book_for_massage'),
]
