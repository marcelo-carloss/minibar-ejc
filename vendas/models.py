from django.db import models
from produtos.models import Produto
from pessoas.models import Pessoa
from django.contrib.auth.models import User

class Venda(models.Model):
    class FormaPagamento(models.TextChoices):
        PIX = 'PIX', 'Pix'
        DINHEIRO = 'DIN', 'Dinheiro'
        CARTAO = 'CAR', 'Cartao'

    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario_praticado = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    usuario_ultima_atualizacao = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='vendas_atualizadas')
    pago = models.BooleanField(default=False)
    forma_pagamento = models.CharField(choices=FormaPagamento.choices, max_length=3, blank=True)
    data_pagamento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pessoa.nome} ({self.pessoa.get_circulo_dispaly()}) | Prod:  | {self.produto.nome} |  Qtnd:  | {self.quantidade} |"