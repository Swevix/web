# cars/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def compare(request):
    return render(request, 'compare.html')

def cars_list(request):
    return render(request, 'cars.html')

def car_detail(request, car_id):
    return HttpResponse(f"<h1>Информация о машине</h1><p>ID: {car_id}</p>")

