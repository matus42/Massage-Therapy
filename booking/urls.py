from django.urls import path
from .views import book_appointment, get_available_time_slots

urlpatterns = [
    path('get_available_time_slots/', get_available_time_slots, name='get_available_time_slots'),
    path('', book_appointment, name='book_appointment'),
]
