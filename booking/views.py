from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

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
            messages.success(request, 'Your booking has been successfully made!')
            return redirect('book_appointment')
    else:
        form = BookingForm()
    return render(request, 'booking/book_appointment.html', {'form': form})
