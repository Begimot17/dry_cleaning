from django.shortcuts import render

def index(request):
    return render(request, 'manager/index.html')
def orders(request):
    return render(request, 'manager/orders.html')
def orders_done(request):
    return render(request, 'manager/orders_done.html')
def possession(request):
    return render(request, 'manager/possession.html')
def shift(request):
    return render(request, 'manager/shift.html')
def dir_drugs(request):
    return render(request, 'manager/dir_drugs.html')
def dir_serv(request):
    return render(request, 'manager/dir_serv.html')
