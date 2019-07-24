from django import forms

from bdo_gestor_guilda.core.models.payout import Payout


class PayoutForm(forms.ModelForm):
    class Meta:
        model = Payout
        fields = ['data_inicio', 'data_fim']
        labels = {
            'data_inicio': 'Data Início Período do Payout',
            'data_fim': 'Data Fim Período do Payout',
        }
        widgets = {
            'data_inicio': forms.TextInput(
                attrs={'class': 'form-control date-picker-default', 'placeholder': 'dd/mm/yyyy', 'required': True}),
            'data_fim': forms.TextInput(
                attrs={'class': 'form-control date-picker-default', 'placeholder': 'dd/mm/yyyy', 'required': True}),
        }
