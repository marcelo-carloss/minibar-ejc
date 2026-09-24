from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['nome', 'circulo']
        labels = {
            'nome': 'Nome',
            'circulo': 'Circulo',
        }

