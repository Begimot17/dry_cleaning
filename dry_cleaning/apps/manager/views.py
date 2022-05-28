from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from receiver.models import *
from authorize.models import Profile
from django.http import HttpResponseRedirect
from datetime import date

def index(request):
    return render(request, 'manager/index.html')


def orders(request):
    a = Order.objects.all()
    list=[]
    for ord in a:
        if ord.status != "Success":
            list.append(ord)
    config = {
        'orders': list
    }
    return render(request, 'manager/orders.html',config)


def order_done(request,id):
    order = Order.objects.get(id=id)
    order.status ="Success"
    order.date_of_issue = date.today()
    order.save()
    return HttpResponseRedirect(reverse('manager:orders'))


def orders_done(request):
    a = Order.objects.all()
    list = []
    for ord in a:
        if ord.status == "Success":
            list.append(ord)
    config = {
        'orders': list
    }
    return render(request, 'manager/orders_done.html',config)


def possession(request):
    a = Possession.objects.all()
    config = {
        'possessions': a
    }
    return render(request, 'manager/possession.html', config)

def add_possession(request):

    return render(request, 'manager/add_possession.html', )

def upd_possession(request, id):
    drug = Possession.objects.get(id=id)
    config = {
        'poss': drug,
    }
    return render(request, 'manager/upd_possession.html', config)


def update_possession(request, id):
    possession = Possession.objects.get(id=id)
    possession.name = request.POST['name']
    possession.type = request.POST['type']
    possession.service = request.POST['service']
    possession.chemical = request.POST['chemical']
    possession.cost = request.POST['cost']
    possession.hour = request.POST['hour']
    possession.save()
    return HttpResponseRedirect(reverse('manager:possession'))


def del_possession(request, id):
    Possession.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('manager:possession'))


def reg_possession(request):
    profile = Possession.objects.create(name= request.POST['name'],
                                     type=request.POST['type'],
                                   service=request.POST['service'],
                                    chemical = request.POST['chemical'],
                                    cost = request.POST['cost'],
                                    hour = request.POST['hour'],
                                    date = date.today())
    profile.save()
    return HttpResponseRedirect(reverse('manager:possession'))


def shift(request):
    a = Profile.objects.all()
    config = {
        'profiles': a
    }
    return render(request, 'manager/shift.html',config)

def add_shift(request,id):
    prof = Profile.objects.get(id=id)
    prof.total+=1
    prof.save()
    return HttpResponseRedirect(reverse('manager:shift'))


def dir_drugs(request):
    a = Chemicals.objects.all()
    config = {
        'drugs': a
    }
    return render(request, 'manager/dir_drugs.html',config)

def add_drugs(request):
    config = {
    }
    return render(request, 'manager/add_drugs.html', config)

def upd_drugs(request, id):
    drug = Chemicals.objects.get(id=id)
    config = {
        'drug': drug,
    }
    return render(request, 'manager/upd_drugs.html', config)


def update_drugs(request, id):
    drug = Chemicals.objects.get(id=id)
    drug.name = request.POST['name']
    drug.quantity = request.POST['quantity']
    drug.type = request.POST['type']
    drug.type_by_use = request.POST['type_by_use']
    drug.instruction = request.POST['instruction']
    drug.save()
    return HttpResponseRedirect(reverse('manager:dir_drugs'))


def del_drugs(request, id):
    Chemicals.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('manager:dir_drugs'))


def reg_drugs(request):
    profile = Chemicals.objects.create(name= request.POST['name'],
                                     quantity=request.POST['quantity'],
                                   type=request.POST['type'],
                                    type_by_use = request.POST['type_by_use'],
                                    instruction = request.POST['instruction'])
    profile.save()
    return HttpResponseRedirect(reverse('manager:dir_drugs'))


def add_servs(request):
    return render(request, 'manager/add_servs.html')


def dir_servs(request):
    a = Service.objects.all()
    config = {
        'servs': a
    }
    return render(request, 'manager/dir_servs.html', config)


def upd_servs(request, id):
    service = Service.objects.get(id=id)
    config = {
        'serv': service
    }
    return render(request, 'manager/upd_servs.html', config)


def update_servs(request, id):
    service = Service.objects.get(id=id)
    service.time = request.POST['time']
    service.ownership = request.POST['ownership']
    service.preparations = request.POST['preparations']
    service.total = request.POST['total']
    service.save()
    return HttpResponseRedirect(reverse('manager:dir_servs'))


def del_servs(request, id):
    Service.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('manager:dir_servs'))


def reg_servs(request):
    profile = Service.objects.create(name=request.POST['name'],
                                     time=request.POST['time'],
                                     ownership=request.POST['ownership'],
                                     preparations=request.POST['preparations'],
                                     total=request.POST['total'])
    profile.save()
    return HttpResponseRedirect(reverse('manager:dir_servs'))
