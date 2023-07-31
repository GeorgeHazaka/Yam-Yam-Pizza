from django.contrib import admin
from .models import Booking, Pizza
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('username', 'email', 'persons_number', 'table_number', 'booked_on')
    search_fields = ['username', 'persons_number', 'table_number']
    prepopulated_fields = {'slug': ('username',)}
    list_filter = ('booked_on', 'persons_number')


@admin.register(Pizza)
class PizzaAdmin(SummernoteModelAdmin):

    list_display = ('name', 'price')
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('price',)
