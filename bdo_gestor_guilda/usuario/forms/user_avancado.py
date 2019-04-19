from django import forms

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class UserAvancadoForm(forms.ModelForm):
    class Meta:
        model = UserAvancado
        fields = ['__all__']
        labels = {
            'user_discord': 'Nome de Usuário do Discord(FULANO#6666)',
            'nome_familia': 'Nome da Família',
            'nome_char_principal': 'Nome do Char Principal',
            'char_lvl': 'Level Char Principal',
            'char_classe': 'Classe Char Principal',
            'char_ap': 'PA Char Principal',
            'char_ap_despertada': 'PA Despertado Char Principal',
            'char_dp': 'PD Char Principal',
            'gs': 'GS Char Principal((PA + PA AWK)/2 + PD)',
            'url_print_status': 'URL de um Print da Tela Inteira com seu PA e PD(Dica: Use Discord para obter URL)'
        }
