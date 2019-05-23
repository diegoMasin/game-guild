from django import forms

from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos


class VinculoGruposForm(forms.ModelForm):
    class Meta:
        model = VinculoGrupos
        fields = ['membro', 'grupo']
        labels = {
            'membro': 'Escolha um Membro para Party',
            'grupo': 'Escolha a Party',
        }
        widgets = {
            'membro': forms.Select(attrs={'class': 'form-control select2', 'required': True}),
            'grupo': forms.Select(attrs={'class': 'form-control select2', 'required': True}),
        }
