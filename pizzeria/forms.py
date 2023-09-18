from django import forms
from .models import Booking


class BookTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('email', 'number_of_persons',
                  'table_number', 'date', 'time')
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                }
            ),
        }
