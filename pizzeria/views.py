from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pizza, Booking
from .forms import BookTableForm
from django.contrib import messages
from datetime import datetime, timedelta
from django import forms


class Home(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.order_by('price')
    template_name = 'home.html'


class PizzaList(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.order_by('price')
    template_name = 'menu.html'
    paginate_by = 12


class PizzaDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Pizza.objects
        pizza = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'pizza_details.html',
            {
                'pizza': pizza,
            }
        )


class BookTable(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):

        has_booking = Booking.objects.filter(username=request.user.username)

        if has_booking:
            return render(
                request,
                'booking_submitted.html',
                {
                    'booking': has_booking,
                }
            )

        else:
            return render(
                request,
                'book_table.html',
                {
                    'booked': False,
                    'book_table_form': BookTableForm(),
                },
            )

    def post(self, request, *args, **kwargs):

        book_table_form = BookTableForm(data=request.POST)

        if request.method == "POST":
            form = BookTableForm(request.POST)

            if form.is_valid():
                table_number = request.POST['table_number']
                datetime = form.cleaned_data['datetime']
                time_difference = datetime - timedelta(hours=1)

                existing_bookings = Booking.objects.filter(
                    table_number=table_number,
                    datetime=time_difference
                )

                if existing_bookings.exists():
                    messages.error(request, "Table Already Booked")
                    return render(
                        request,
                        'book_table.html',
                        {
                            'book_table_form': BookTableForm(),
                        }
                    )

        if book_table_form.is_valid():
            book_table_form.instance.username = request.user.username
            book_table = book_table_form.save(commit=False)
            book_table.save()
        else:
            book_table_form = BookTableForm()

        return render(
            request,
            'book_table.html',
            {
                'booked': True,
                'book_table_form': BookTableForm(),
            },
        )


class FillTableForm(CreateView):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book_table.html',
            {
                'booked': False,
                'book_table_form': BookTableForm(),
            },
        )

    def post(self, request, *args, **kwargs):

        book_table_form = BookTableForm(data=request.POST)

        if request.method == "POST":
            form = BookTableForm(request.POST)

            if form.is_valid():
                table_number = request.POST['table_number']
                datetime = form.cleaned_data['datetime']

                existing_bookings = Booking.objects.filter(
                    table_number=table_number,
                    datetime__range=(datetime - timedelta(minutes=59), datetime + timedelta(minutes=59))
                )

                if existing_bookings.exists():
                    messages.error(request, "Sorry, Table is already booked")
                    return render(
                        request,
                        'book_table.html',
                        {
                            'book_table_form': BookTableForm(),
                        }
                    )

        if book_table_form.is_valid():
            book_table_form.instance.username = request.user.username
            book_table = book_table_form.save(commit=False)
            book_table.save()
        else:
            book_table_form = BookTableForm()

        return render(
            request,
            'book_table.html',
            {
                'booked': True,
                'book_table_form': BookTableForm(),
            },
        )


class UpdateBooking(UpdateView):

    model = Booking
    form_class = BookTableForm
    template_name = 'update_booking.html'

    def form_valid(self, form):
        form.save()
        return redirect('book_table')
