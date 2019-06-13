from django import forms

from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra


class ParticiparGuerraForm(forms.ModelForm):
    class Meta:
        model = ParticiparGuerra
        fields = ['guerra', 'participa', 'participante']
        labels = {
            'participa': 'Participará da Guerra?',
        }
        widgets = {
            'guerra': forms.HiddenInput(),
            'participante': forms.HiddenInput(),
            'participa': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }
