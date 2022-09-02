from django.urls import path
from telefonicapp import views

urlpatterns = [
    path('', views.index, name= 'index')
]