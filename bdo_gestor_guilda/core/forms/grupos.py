from django import forms

from bdo_gestor_guilda.core.models.grupos import Grupos


class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['lider', 'titulo', 'tipo_guerra']
        labels = {
            'lider': 'Líder da Party',
            'titulo': 'Título da Party',
            'tipo_guerra': 'Tipo de Guerra',
        }
        widgets = {
            'lider': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'tipo_guerra': forms.Select(attrs={'class': 'form-control'}),
        }
