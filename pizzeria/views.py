from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pizza, Booking
from .forms import BookTableForm
from django.contrib.auth.decorators import login_required


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
                "pizza": pizza,
            }
        )


class BookTable(LoginRequiredMixin, CreateView):
 
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'book_table.html',
            {
                "booked": False,
                "book_table_form": BookTableForm(),
            },
        )

    def post(self, request, *args, **kwargs):

        book_table_form = BookTableForm(data=request.POST)

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
                "booked": True,
                "book_table_form": BookTableForm(),
            },
        )

# class BookTable(CreateView):

#     def get(self, request, *args, **kwargs):
#         queryset = Booking.objects
#         booking = get_object_or_404(queryset, slug=slug)

#         return render(
#             request,
#             'book_table.html',
#             {
#                 "book_table_form": BookTableForm(),
#             },
#         )

#     def post(self, request, *args, **kwargs):
#         queryset = Booking.objects
#         booking = get_object_or_404(queryset, slug=slug)
#         book_table_form = BookTableForm()

#         return render(
#             request,
#             'book_table.html',
#             {
#                 "book_table_form": BookTableForm(),
#             },
#         )
