from django import forms

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar
from bdo_gestor_guilda.core.helpers.utils import normaliza_texto


class TipoClasseCharForm(forms.ModelForm):
    class Meta:
        model = TipoClasseChar
        fields = ['nome_classe', 'slug']
        labels = {
            'slug': 'Nome da Classe',
        }
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

    def clean_nome_classe(self):
        cleaned = self.cleaned_data.get('slug')
        return normaliza_texto(cleaned)
