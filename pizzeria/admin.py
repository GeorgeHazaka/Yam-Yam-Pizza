from django.contrib import admin
from .models import Booking, Pizza
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients')
    list_display = (
        'username', 'slug', 'email',
        'number_of_persons', 'table_number', 'datetime'
    )
    search_fields = ['username', 'number_of_persons', 'table_number']
    prepopulated_fields = {'slug': ('username',)}
    list_filter = ('datetime', 'number_of_persons')


@admin.register(Pizza)
class PizzaAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'price')
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('price',)
