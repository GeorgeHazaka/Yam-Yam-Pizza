from django.contrib import admin
from .models import Booking, Pizza
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients')
    list_display = (
        'username', 'slug', 'email',
        'persons_number', 'table_number', 'date', 'time'
    )
    search_fields = ['username', 'persons_number', 'table_number']
    prepopulated_fields = {'slug': ('username',)}
    list_filter = ('date', 'time', 'persons_number')


@admin.register(Pizza)
class PizzaAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'price')
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('price',)
