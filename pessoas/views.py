from django.shortcuts import render
from .models import Pessoa

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/listar.html', {'pessoas': pessoas})