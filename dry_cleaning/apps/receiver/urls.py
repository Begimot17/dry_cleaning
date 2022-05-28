from django.urls import path
from . import views

app_name = 'receiver'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_clients/', views.add_clients, name='add_clients'),
    path('reg_clients/', views.reg_clients, name='reg_clients'),
    path('upd_clients/<int:id>', views.upd_clients, name='upd_clients'),
    path('update_clients/<int:id>', views.update_clients, name='update_clients'),
    path('del_clients/<int:id>', views.del_clients, name='del_clients'),
    path('clients/', views.clients, name='clients'),


    path('services/', views.services, name='services'),
    path('add_services/', views.add_services, name='add_services'),
    path('reg_services/', views.reg_services, name='reg_services'),
    path('services_done/', views.services_done, name='services_done'),
    path('upd_services/<int:id>', views.upd_services, name='upd_services'),
    path('update_services/<int:id>', views.update_services, name='update_services'),
    path('del_services/<int:id>', views.del_services, name='del_services'),


    path('orders/', views.orders, name='orders'),
    path('add_order/', views.add_order, name='add_order'),
    path('reg_orders/', views.reg_orders, name='reg_orders'),
    path('upd_orders/<int:id>', views.upd_orders, name='upd_orders'),
    path('update_orders/<int:id>', views.update_orders, name='update_orders'),
    path('del_orders/<int:id>', views.del_orders, name='del_orders')
]
