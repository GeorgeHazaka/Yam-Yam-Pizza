from django.shortcuts import render
from django.views import generic
from .models import Pizza


class Home(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.order_by('price')
    template_name = 'home.html'


class PizzaList(generic.ListView):
    model = Pizza
    queryset = Pizza.objects.order_by('price')
    template_name = 'menu.html'
    paginate_by = 12
