from django import forms

from bdo_gestor_guilda.core.models.anuncios_gerais import AnunciosGerais


class AnunciosGeraisForm(forms.ModelForm):
    class Meta:
        model = AnunciosGerais
        fields = ['texto']
        labels = {
            'texto': 'Digite o texto do Anúncio',
        }
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
