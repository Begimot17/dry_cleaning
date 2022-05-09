from django.urls import path
from . import views

app_name = 'receiver'

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('add_order/', views.add_order, name='add_order'),
    path('services/', views.services, name='services'),
    path('services_done/', views.services_done, name='services_done'),
    path('orders/', views.orders, name='orders')
]
