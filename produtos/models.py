from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco_padrao = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome