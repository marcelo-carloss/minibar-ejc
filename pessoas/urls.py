from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
    path('criar/', views.criar_pessoa, name='criar_pessoa'),
    path('editar/<int:pessoa_id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir/<int:pessoa_id>/', views.excluir_pessoa, name='excluir_pessoa'),
]