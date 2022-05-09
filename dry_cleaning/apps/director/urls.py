from django.urls import path
from . import views

app_name = 'director'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
path('analysis/', views.analysis, name='analysis'),
path('accounting/', views.accounting, name='accounting')
]
