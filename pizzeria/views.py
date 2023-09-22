from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
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
            table_number = request.POST['table_number']
            date = book_table_form.instance.date
            time = book_table_form.instance.time
            print(date)
            print(time)
            if Booking.objects.filter(table_number=table_number).exists():
                if Booking.objects.filter(date=date).exists():
                    if Booking.objects.filter(time__lte=time, time__gte=time + timedelta(minutes=59)).exists():
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
            table_number = request.POST['table_number']
            date = book_table_form.instance.date
            time = book_table_form.instance.time
            print(date)
            print(time)

            if Booking.objects.filter(table_number=table_number).exists() and Booking.objects.filter(date=date).exists() and Booking.objects.filter(time__lte = time, time__gte = time + timedelta(minutes=59)).exists():
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
