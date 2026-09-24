from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'pessoa', 'quantidade', 'preco_unitario_praticado']
        labels = {
            'produto': 'Produto',
            'pessoa': 'Pessoa',
            'quantidade': 'Quantidade',
            'preco_unitario_praticado': 'Preço (R$)'
        }

    def clean_preco_unitario_praticado(self):
        preco = self.cleaned_data.get('preco_unitario_praticado')
        if preco < 0.0:
            raise forms.ValidationError('O preço deve ser maior que zero.')
        return preco