from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
import json

from .models import Venda
from .forms import VendaForm
from produtos.models import Produto


def listar_vendas(request):
    vendas = Venda.objects.select_related('produto', 'pessoa','usuario').all()
    return render(request, 'vendas/listar.html', {'vendas': vendas})

@login_required
def criar_venda(request):
    produtos_json = _montar_produtos_json()

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.usuario = request.user
            venda.usuario_ultima_atualizacao = request.user
            venda.save()
            return redirect(
                'listar_vendas'
            )

    else:
        form = VendaForm()

    return render(request, 'vendas/form.html', {'form':form, 'produtos_json':produtos_json})

@login_required
def editar_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)

    produtos_json = _montar_produtos_json()

    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.usuario_ultima_atualizacao = request.user
            venda.save()
            return redirect(
                'listar_vendas'
            )

    else:
        form = VendaForm(instance=venda)

    return render(request, 'vendas/form.html', {'form':form, 'produtos_json':produtos_json})

@login_required
def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    if request.method == 'POST':
        venda.delete()
        return redirect(
            'listar_vendas'
        )

    else:
        return render(request, 'vendas/confirmar_exclusao.html', {'venda':venda})

def _montar_produtos_json():
    lista_produtos = list(Produto.objects.all().values("id", "nome", "preco_padrao"))
    for p in lista_produtos:
        if isinstance(p["preco_padrao"], Decimal):
            p["preco_padrao"] = str(p["preco_padrao"])
    return json.dumps(lista_produtos, indent=4, ensure_ascii=False)