from django.shortcuts import render

def index(request):
    return render(request, 'director/index.html')

def register(request):
    return render(request, 'director/reg.html')
def accounting(request):
    return render(request, 'director/accounting.html')
def analysis(request):
    return render(request, 'director/analysis.html')