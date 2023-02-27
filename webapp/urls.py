from django.urls import path

from webapp.views import index, about, services, cars, contact

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('cars/', cars, name='cars'),
    path('contact/', contact, name='contact'),

]
