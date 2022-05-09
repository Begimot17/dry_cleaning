from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('dir_drugs/', views.dir_drugs, name='dir_drugs'),
    path('dir_serv/', views.dir_serv, name='dir_serv'),
    path('orders/', views.orders, name='orders'),
    path('orders_done/', views.orders_done, name='orders_done'),
    path('possession/', views.possession, name='possession'),
    path('shift/', views.shift, name='shift')
]
