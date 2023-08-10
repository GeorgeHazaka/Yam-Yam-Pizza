from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu/', views.PizzaList.as_view(), name='menu'),
    # path('', views.home, name='home'),
]
