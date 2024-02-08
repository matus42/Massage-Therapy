from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking

# Create your views here.


# Decorator to check if the user is logged in
@login_required(login_url='/accounts/login/')
def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, 'Your booking has been successfully made!')
            return redirect('book_appointment')
    else:
        form = BookingForm()
    return render(request, 'booking/book_appointment.html', {'form': form})


def get_available_time_slots(request):
    date = request.GET.get('date')
    booked_slots = Booking.objects.filter(date=date).values_list('time_slot', flat=True)
    all_slots = [
        ('9AM-10AM', '9AM-10AM'), ('10AM-11AM', '10AM-11AM'),
        ('11AM-12PM', '11AM-12PM'), ('1PM-2PM', '1PM-2PM'),
        ('2PM-3PM', '2PM-3PM'), ('3PM-4PM', '3PM-4PM'),
        ('4PM-5PM', '4PM-5PM'),
    ]
    available_slots = [slot for slot in all_slots if slot[0] not in booked_slots]

    if not available_slots:
        return JsonResponse({'message': 'Fully booked', 'available_slots': []})
    else:
        return JsonResponse({'available_slots': available_slots})
