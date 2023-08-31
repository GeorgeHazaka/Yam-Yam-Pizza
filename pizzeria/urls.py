from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu/', views.PizzaList.as_view(), name='menu'),
    # path('book-table/', views.BookTable.as_view(), name='book_table'),
    path('<slug:slug>/', views.PizzaDetails.as_view(), name='pizza_details'),
]
