from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
