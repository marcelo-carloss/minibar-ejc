from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F

from pessoas.models import Pessoa
from vendas.models import Venda


def buscar_pessoas(request):
    nome_pesquisado = request.GET.get('nome')

    if nome_pesquisado:
        pessoa = Pessoa.objects.filter(nome__icontains=nome_pesquisado)
    else:
        pessoa = Pessoa.objects.all()
    return render(request, 'consultas/resultado_busca_pessoa.html', {'pessoa': pessoa})

def detalhe_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    vendas = Venda.objects.filter(pessoa=pessoa).select_related('produto')

    resultado_total = vendas.aggregate(total=Sum(F('quantidade') * F('preco_unitario_praticado')))
    valor_total = resultado_total['total'] or 0

    resultado_pendente = vendas.filter(pago=False).aggregate(total_pendente=Sum(F('quantidade') * F('preco_unitario_praticado')))
    valor_pendente = resultado_pendente['total_pendente'] or 0

    return render(request, 'consultas/resultado_detalhe_pessoa.html',{'pessoa': pessoa, 'vendas': vendas, 'valor_total': valor_total, 'valor_pendente': valor_pendente})


