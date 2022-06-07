from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseRedirect
from datetime import date

class Client_info(object):
    def __init__(self,client, count, total, date):
        """Constructor"""
        self.client = client
        self.count = count
        self.total = total
        self.date = date
def index(request):
    return render(request, 'receiver/index.html')


def add_clients(request):
    return render(request, 'receiver/add_clients.html')


def upd_clients(request, id):
    client = Client.objects.get(id=id)
    config = {
        'client': client
    }
    return render(request, 'receiver/upd_clients.html', config)


def update_clients(request, id):
    client = Client.objects.get(id=id)
    user = client.user
    user.last_name = request.POST['last_name']
    user.first_name = request.POST['first_name']
    client.phone = request.POST['phone']
    user.save()
    client.save()
    return HttpResponseRedirect(reverse('receiver:clients'))


def del_clients(request, id):
    Client.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('receiver:clients'))


def reg_clients(request):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(username=request.POST['phone'],
                                         first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'])
    user.save()
    profile = Client.objects.create(user=user,
                                    phone=request.POST['phone'])
    profile.save()
    return HttpResponseRedirect(reverse('receiver:clients'))


def clients(request):
    client = Client.objects.all()
    clients = []
    orders = Order.objects.all()
    for cli in client:
        count = 0
        total = 0
        date = 0
        for ord in orders:
            if ord.client == cli:
                count += 1
                total += ord.total
                if date == 0:
                    date = ord.date_of_issue
                if date < ord.date_of_issue:
                    date = ord.date_of_issue
        clients.append(Client_info(cli, count, total, date))

    config = {
        'clients': clients
    }
    return render(request, 'receiver/clients.html', config)


def add_services(request):
    return render(request, 'receiver/add_services.html')


def services(request):
    a = Service.objects.all()
    config = {
        'services': a
    }
    return render(request, 'receiver/services.html', config)


def upd_services(request, id):
    service = Service.objects.get(id=id)
    config = {
        'service': service
    }
    return render(request, 'receiver/upd_services.html', config)

def reg_services(request):
    profile = Service.objects.create(name=request.POST['name'],
                                     time=request.POST['time'],
                                     ownership=request.POST['ownership'],
                                   preparations=request.POST['preparations'],
                                    total = request.POST['total'])
    profile.save()
    return HttpResponseRedirect(reverse('receiver:services'))


def update_services(request, id):
    service = Service.objects.get(id=id)
    service.time = request.POST['time']
    service.ownership = request.POST['ownership']
    service.preparations = request.POST['preparations']
    service.total = request.POST['total']
    service.save()
    return HttpResponseRedirect(reverse('receiver:services'))


def del_services(request, id):
    Service.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('receiver:services'))


def reg(request):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    """ client= Client.objects.create(user=user,email=request.POST['email'],
                                  first_name=request.POST['first_name'],
                                  last_name=request.POST['last_name'])
    client.save() """
    return HttpResponseRedirect(reverse('accounts:index'))


def services_done(request):
    return render(request, 'receiver/services_done.html')

def orders(request):
    a = Order.objects.all()
    config = {
        'orders': a
    }
    return render(request, 'receiver/orders.html', config)


def add_order(request):
    a = Client.objects.all()
    b = Service.objects.all()
    config = {
        'clients': a,
        'services': b
    }
    return render(request, 'receiver/add_order.html', config)

def upd_orders(request, id):
    order = Order.objects.get(id=id)
    a = Client.objects.all()
    b = Service.objects.all()
    config = {
        'order': order,
        'clients': a,
        'services': b
    }
    return render(request, 'receiver/upd_orders.html', config)


def update_orders(request, id):
    order = Order.objects.get(id=id)
    order.client = Client.objects.get(id=request.POST['client'])
    order.quantity = request.POST['quantity']
    order.clothes = request.POST['clothes']
    order.total = request.POST['total']
    order.service = Service.objects.get(id=request.POST['service'])
    order.save()
    return HttpResponseRedirect(reverse('receiver:orders'))


def del_orders(request, id):
    Order.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('receiver:orders'))


def reg_orders(request):
    profile = Order.objects.create(client= Client.objects.get(id=request.POST['client']),
                                     quantity=request.POST['quantity'],
                                   clothes=request.POST['clothes'],
                                    total = request.POST['total'],
                                    service = Service.objects.get(id=request.POST['service']),
                                   date_of_issue=date.today())
    profile.save()
    return HttpResponseRedirect(reverse('receiver:orders'))
