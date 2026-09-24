from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_vendas, name='listar_vendas'),
    path('criar/', views.criar_venda, name='criar_venda'),
    path('editar/<int:venda_id>/', views.editar_venda, name='editar_venda'),
    path('excluir/<int:venda_id>/', views.excluir_venda, name='excluir_venda'),
]