from django import forms

from bdo_gestor_guilda.core.models.grupos import Grupos


class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['lider', 'titulo']
        labels = {
            'lider': 'Escolha o Líder da Party',
            'titulo': 'Título da Party',
        }
        widgets = {
            'lider': forms.Select(attrs={'class': 'form-control select2', 'required': True}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
