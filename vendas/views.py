from django.shortcuts import render

from .models import Venda


def listar_vendas(request):
    vendas = Venda.objects.select_related('produto', 'pessoa','usuario').all()
    return render(request, 'vendas/listar.html', {'vendas': vendas})
