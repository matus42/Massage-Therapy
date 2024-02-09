from django.urls import path
from .views import book_appointment, get_available_time_slots, user_info

urlpatterns = [
    path('get_available_time_slots/', get_available_time_slots, name='get_available_time_slots'),
    path('user_info/', user_info, name='user_info'),
    path('', book_appointment, name='book_appointment'),
]
