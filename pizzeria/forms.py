from django import forms
from .models import Booking
# from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class BookTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('username', 'email', 'persons_number',
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
