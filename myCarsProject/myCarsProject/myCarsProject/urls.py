# myCarsProject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем urls из приложения cars
    path('', include('cars.urls')),
]
