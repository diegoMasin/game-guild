from django import forms

from bdo_gestor_guilda.core.models.guerras import Guerras


class GuerrasForm(forms.ModelForm):
    class Meta:
        model = Guerras
        fields = ['tipo', 'modelo', 'data_inicio', 'call', 'pt_fixa', 'quantidade_players', 'servidor', 'node']
        labels = {
            'tipo': 'Guerra',
            'modelo': 'Estilo de Guerra',
            'data_inicio': 'Dia da Guerra',
            'call': 'Call de ...',
            'pt_fixa': 'PT Fixa',
            'quantidade_players': 'Nº Máximo de Players',
            'servidor': 'Qual Servidor',
            'node': 'Nome do Node da Guerra',
        }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'modelo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'data_inicio': forms.TextInput(
                attrs={'class': 'form-control date-picker-default', 'placeholder': 'dd/mm/yyyy', 'required': True}),
            'call': forms.Select(attrs={'class': 'form-control select2'}),
            'pt_fixa': forms.Select(choices=((True, 'Sim'), (False, 'Não')), attrs={'class': 'form-control'}),
            'quantidade_players': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'servidor': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'node': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
