from django import forms
from .models import Booking
from datetime import datetime


class BookTableForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('email', 'number_of_persons',
                  'table_number', 'datetime')
        widgets = {
            'datetime': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'min': datetime.now().strftime('%Y-%m-%dT%H:%M'),
                }
            )
        }
