from . import views
from django.urls import path

urlpatterns = [
    path('', views.PizzaList.as_view(), name='home')
]