from django.shortcuts import render
from django.views import generic
from .models import Pizza


class PizzaList(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.order_by('price')
    template_name = 'index.html'
    paginate_by = 10
