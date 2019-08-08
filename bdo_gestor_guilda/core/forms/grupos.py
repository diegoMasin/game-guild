from django import forms

from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class GruposForm(forms.ModelForm):
    lider = forms.ModelChoiceField(
        label='Escolha o Líder da Party',
        queryset=UserAvancado.objects.filter(ativo=True),
        widget=forms.Select(attrs={'class': 'form-control select2', 'required': True})
    )

    class Meta:
        model = Grupos
        fields = ['lider', 'titulo']
        labels = {
            'titulo': 'Título da Party',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
