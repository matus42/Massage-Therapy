from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['massage', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book Now'))
        self.fields['date'].input_formats = ('%Y-%m-%d',)

    def clean_date(self):
        date = self.cleaned_data['date']
        today = timezone.localdate()
        if date < today:
            raise ValidationError("Booking for past dates is not allowed.")
        return date