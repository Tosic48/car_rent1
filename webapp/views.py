from django.shortcuts import render
from django.core.paginator import Paginator
from webapp.models import Car

def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def services(request):
    return render(request, 'webapp/services.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 4)
    page_number = request.GET.get('page')

    context = {'cars': cars}
    return render(request, 'webapp/cars.html')
