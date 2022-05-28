from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('dir_drugs/', views.dir_drugs, name='dir_drugs'),
    path('add_drugs/', views.add_drugs, name='add_drugs'),
    path('reg_drugs/', views.reg_drugs, name='reg_drugs'),
    path('upd_drugs/<int:id>', views.upd_drugs, name='upd_drugs'),
    path('update_drugs/<int:id>', views.update_drugs, name='update_drugs'),
    path('del_drugs/<int:id>', views.del_drugs, name='del_drugs'),

    path('dir_servs/', views.dir_servs, name='dir_servs'),
    path('add_servs/', views.add_servs, name='add_servs'),
    path('reg_servs/', views.reg_servs, name='reg_servs'),
    path('upd_servs/<int:id>', views.upd_servs, name='upd_servs'),
    path('update_servs/<int:id>', views.update_servs, name='update_servs'),
    path('del_servs/<int:id>', views.del_servs, name='del_servs'),

    path('orders/', views.orders, name='orders'),
    path('order_done/<int:id>', views.order_done, name='order_done'),


    path('orders_done/', views.orders_done, name='orders_done'),


    path('possession/', views.possession, name='possession'),
    path('add_possession/', views.add_possession, name='add_possession'),
    path('reg_possession/', views.reg_possession, name='reg_possession'),
    path('upd_possession/<int:id>', views.upd_possession, name='upd_possession'),
    path('update_possession/<int:id>', views.update_possession, name='update_possession'),
    path('del_possession/<int:id>', views.del_possession, name='del_possession'),



    path('shift/', views.shift, name='shift'),
    path('add_shift/<int:id>', views.add_shift, name='add_shift')
]
