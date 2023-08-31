from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import FormView
# maybe FormView not needed
from .models import Pizza, Booking
from .forms import BookTableForm


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


# class BookTable(FormView):

#     def post(self, request, *args, **kwargs):
#         queryset = Booking.objects
#         booking = get_object_or_404(queryset, slug=slug)
#         template_name = 'book_table.html'
#         form_class = BookTableForm
#         book_table_form = BookTableForm(data=request.POST)

#         return render(
#             request,
#             'book_table.html',
#             {
#                 "book_table_form": BookTableForm(),
#             }
#         )

# def book_table(request):

#     context = {}

#     return render(request, 'Pizzeria/book_table.html', context)
