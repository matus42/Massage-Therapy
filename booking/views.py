from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking
from treatments.models import Massage


@login_required(login_url='/accounts/login/')
def book_appointment(request, massage_id=None):
    """
    Book a massage appointment.

    - If `massage_id` is given, pre-selects that massage.
    - On POST: processes the booking form.
    - On GET: displays an empty or pre-filled booking form based on
      massage_id.
    - Requires login.

    Args:
        request: The HTTP request.

    Returns:
        The booking page with the form.
    """
    massage = get_object_or_404(Massage, id=massage_id) if massage_id else None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            if massage:
                booking.massage = massage
            booking.save()
            messages.success(request,
                             'Your booking has been successfully made!')
            return redirect('book_appointment')
    else:
        form = (BookingForm(initial={'massage': massage})
                if massage else BookingForm())

    return render(request, 'booking/book_appointment.html',
                  {'form': form, 'massage': massage})


def get_available_time_slots(request):
    """
    Get available booking time slots for a given date.

    Args:
        request: HttpRequest object containing the date parameter.

    Returns:
        JsonResponse with a list of available time slots or a message
        indicating fully booked.
    """
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
    """
    Edit an existing booking.

    Loads the booking for the given `booking_id`,
    allows the user to edit it, and saves the changes.
    Displays a success message and redirects on successful update.

    Args:
        request: HttpRequest object.
        booking_id: ID of the booking to be edited.

    Returns:
        The booking edit page with the booking form pre-filled with
        existing booking details.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.status = 'pending'
            form.save()
            messages.success(request,
                             'Your booking has been successfully updated!')
            return redirect('user_info')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    """
    Delete a specific booking.

    Only allows deletion if the user is a superuser
    or the owner of the booking.
    Shows a success message if deleted,
    or an error message for unauthorized attempts.

    Args:
        request: HttpRequest object.
        booking_id: ID of the booking to delete.

    Returns:
        Redirects to the 'user_info' page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user.is_superuser or request.user == booking.user:
        booking.delete()
        messages.success(request, 'Booking successfully deleted.')
    else:
        messages.error(request,
                       'You do not have permission to delete this booking.')
    return redirect('user_info')


@login_required
def user_info(request):
    """
    Display the user's booking information.

    Shows all bookings for superusers or only
    the bookings for the logged-in user.
    Orders bookings by date and time slot, descending.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered 'user_info.html' template with bookings context.
    """
    if request.user.is_superuser:
        bookings = Booking.objects.all().order_by('date', 'time_slot')
    else:
        bookings = Booking.objects.filter(user=request.user).order_by(
            '-date', '-time_slot'
            )
    return render(request, 'booking/user_info.html', {'bookings': bookings})


@login_required
def change_booking_status(request, booking_id, new_status):
    """
    Change the status of a booking.

    Only superusers are authorized to change booking statuses.
    Displays a success message upon change, or an error if unauthorized.

    Args:
        request: HttpRequest object.
        booking_id: ID of the booking to change.
        new_status: New status to apply to the booking.

    Returns:
        Redirects to the 'user_info' page.
    """
    if not request.user.is_superuser:
        messages.error(request,
                       "You are not authorized to perform this action.")
        return redirect('user_info')
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.status = new_status
    booking.save()

    messages.success(request, f"Booking status changed to {new_status}.")
    return redirect('user_info')
