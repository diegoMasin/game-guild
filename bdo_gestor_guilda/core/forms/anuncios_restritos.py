from django import forms

from bdo_gestor_guilda.core.models.anuncios_restrito import AnunciosRestritos


class AnunciosRestritosForm(forms.ModelForm):
    class Meta:
        model = AnunciosRestritos
        fields = ['texto']
        labels = {
            'texto': 'Digite o texto do Anúncio',
        }
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
