from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.buscar_pessoas, name='buscar_pessoas'),
    path('pessoa/<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
    path('venda/<int:venda_id>/pagar/', views.marcar_venda_paga, name='marcar_venda_paga'),
    path('pessoa/<int:pessoa_id>/pagar-tudo/', views.marcar_todas_pagas, name='marcar_todas_pagas'),
]