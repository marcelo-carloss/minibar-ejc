from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(
                'listar_produtos',
            )

    else:
        form = ProdutoForm()

    return render(request, 'produtos/form.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            return redirect(
                'listar_produtos',
            )

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/form.html', {'form': form})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect(
            'listar_produtos',
        )

    else:
        return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})