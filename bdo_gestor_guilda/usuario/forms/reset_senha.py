from django import forms


class ResetSenhaForm(forms.Form):
    email = forms.EmailField(
        label='Qual email de cadastro?',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
