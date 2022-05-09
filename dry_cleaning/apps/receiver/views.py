from django.shortcuts import render

def index(request):
    return render(request, 'receiver/index.html')

def clients(request):
    return render(request, 'receiver/clients.html')

def orders(request):
    return render(request, 'receiver/orders.html')

def services(request):
    return render(request, 'receiver/services.html')
def services_done(request):
    return render(request, 'receiver/services_done.html')

def add_order(request):
    return render(request, 'receiver/add_order.html')
