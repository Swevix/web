# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),           # Главная страница
    path('about/', views.about, name='about'),    # О нас
    path('compare/', views.compare, name='compare'),
    path('cars/', views.cars_list, name='cars'),  # Список машин
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),  # Детальная страница машины
]
