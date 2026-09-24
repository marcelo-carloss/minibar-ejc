from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.utils import timezone

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

@login_required
def marcar_venda_paga(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)

    if request.method == 'POST':
        forma_pagamento = request.POST.get('forma_pagamento')
        venda.forma_pagamento = forma_pagamento
        venda.pago = True
        venda.data_pagamento = timezone.now()
        venda.save()

    return redirect('detalhe_pessoa', pessoa_id=venda.pessoa.id)

@login_required
def marcar_todas_pagas(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    if request.method == 'POST':
        forma_pagamento = request.POST.get('forma_pagamento')
        vendas = Venda.objects.filter(pessoa=pessoa, pago=False)
        vendas.update(pago=True, data_pagamento=timezone.now(), forma_pagamento=forma_pagamento)

    return redirect('detalhe_pessoa', pessoa_id=pessoa.id )
