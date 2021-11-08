from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get_city', views.get_city),
    path('get_weather', views.get_weather)
]
