from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.buscar_pessoas, name='buscar_pessoas'),
    path('pessoa/<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
]