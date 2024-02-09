from django.contrib import admin
from .models import Booking
# Register your models here.


# admin.site.register(Booking)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'massage', 'date', 'time_slot', 'status')
    list_filter = ('status', 'date')
    actions = ['approve_bookings', 'reject_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status='approved')
    approve_bookings.short_description = "Mark selected bookings as approved"

    def reject_bookings(self, request, queryset):
        queryset.update(status='rejected')
    reject_bookings.short_description = "Mark selected bookings as rejected"
