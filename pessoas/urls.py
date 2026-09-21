from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
]