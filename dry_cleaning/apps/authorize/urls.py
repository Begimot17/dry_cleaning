from django.urls import path
from . import views

app_name = 'authorize'

urlpatterns = [
    path('',views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('reg/', views.reg, name='reg'),
    path('log/', views.log, name='log'),
    path('log_out/', views.log_out, name='log_out'),
    # url('signup/', SignUpView.as_view(), name='signup'),
    path('getusers/', views.getusers, name='getusers'),
]
