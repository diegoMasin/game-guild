from django import forms

from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class VinculoGruposForm(forms.ModelForm):
    membro = forms.ModelChoiceField(
        label='Escolha um Membro para Party',
        queryset=UserAvancado.objects.filter(ativo=True),
        widget=forms.Select(attrs={'class': 'form-control select2', 'required': True})
    )

    class Meta:
        model = VinculoGrupos
        fields = ['membro', 'grupo']
        labels = {
            'grupo': 'Escolha a Party',
        }
        widgets = {
            'grupo': forms.Select(attrs={'class': 'form-control select2', 'required': True}),
        }
