from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking
from treatments.models import Massage


@login_required(login_url='/accounts/login/')
def book_appointment(request, massage_id=None):
    massage = get_object_or_404(Massage, id=massage_id) if massage_id else None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Set the massage for the booking if a massage was selected
            if massage:
                booking.massage = massage
            booking.save()
            messages.success(request, 'Your booking has been successfully made!')
            return redirect('book_appointment')
    else:
        # Initialize the form with the selected massage if available
        form = BookingForm(initial={'massage': massage}) if massage else BookingForm()

    return render(request, 'booking/book_appointment.html', {'form': form, 'massage': massage})


def get_available_time_slots(request):
    date = request.GET.get('date')
    booked_slots = Booking.objects.filter(
        date=date).values_list('time_slot', flat=True)
    all_slots = [
        ('9am-10am', '9am-10am'), ('10am-11am', '10am-11am'),
        ('11am-12pm', '11am-12pm'), ('1pm-2pm', '1pm-2pm'),
        ('2pm-3pm', '2pm-3pm'), ('3pm-4pm', '3pm-4pm'),
        ('4pm-5pm', '4pm-5pm'),
    ]
    available_slots = [
        slot for slot in all_slots if slot[0] not in booked_slots]

    if not available_slots:
        return JsonResponse({'message': 'Fully booked', 'available_slots': []})
    else:
        return JsonResponse({'available_slots': available_slots})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.status = 'pending'
            form.save()
            messages.success(request, 'Your booking has been successfully updated!')
            return redirect('user_info')  # Redirect to user bookings page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user == booking.user:
        booking.delete()
        messages.success(request, 'Booking successfully deleted.')
    else:
        messages.error(request, 'You do not have permission to delete this booking.')
    return redirect('user_info')



@login_required
def user_info(request):
    user_bookings = Booking.objects.filter(
        user=request.user).order_by('date', 'time_slot')
    return render(request, 'booking/user_info.html', {'bookings': user_bookings})