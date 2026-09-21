from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_padrao']
        labels = {
            'nome': 'Nome',
            'preco_padrao': 'Preço (R$)'
        }
    def clean_preco_padrao(self):
        preco = self.cleaned_data.get('preco_padrao')
        if preco < 0.0:
            raise forms.ValidationError('O preço deve ser maior que zero.')
        return preco