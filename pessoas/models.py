from django.db import models


class Pessoa(models.Model):
    # opções cor do circulo
    class Circulo(models.TextChoices):
        VERMELHO = 'VM', 'Vermelho'
        AZUL = 'AZ', 'Azul'
        AMARELO = 'AM', 'Amarelo'
        LARANJA = 'LA', 'Laranja'
        VERDE = 'VD', 'Verde'

    nome = models.CharField(max_length=50)
    circulo = models.CharField(max_length=2, choices=Circulo.choices, blank=True, null=True)

    def __str__(self):
        return self.nome
