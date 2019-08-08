from django import forms

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class UserAvancadoForm(forms.ModelForm):
    class Meta:
        model = UserAvancado
        fields = ['user_discord', 'nome_familia', 'nome_char_principal', 'char_lvl', 'char_classe', 'char_ap',
                  'char_ap_despertada', 'char_dp', 'gs', 'recruta_para_ser', 'url_print_status', 'siege', 'node_seg',
                  'node_ter', 'node_qua', 'node_qui', 'node_sex', 'node_dom']
        labels = {
            'user_discord': 'ID Discord',
            'nome_familia': 'Nome da Família',
            'nome_char_principal': 'Char Principal',
            'char_lvl': 'Level',
            'char_classe': 'Classe',
            'char_ap': 'PA',
            'char_ap_despertada': 'PA Despertado',
            'char_dp': 'PD',
            'gs': 'GS',
            'url_print_status': 'Print da Tela Inteira do jogo com seu PA e PD',
            'siege': 'Disponível para participar de Siege aos Sábados',
            'recruta_para_ser': 'Candidato para ser',
        }
        widgets = {
            'user_discord': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome_familia': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome_char_principal': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'char_lvl': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_classe': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'char_ap': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_ap_despertada': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_dp': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'gs': forms.TextInput(attrs={'class': 'form-control font-bold text-primary', 'required': True,
                                         'type': 'number', 'readonly': True}),
            'url_print_status': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'siege': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'recruta_para_ser': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }


class UserAvancadoEditarForm(forms.ModelForm):
    class Meta:
        model = UserAvancado
        fields = ['user_discord', 'nome_familia', 'nome_char_principal', 'char_lvl', 'char_classe', 'char_ap',
                  'char_ap_despertada', 'char_dp', 'gs', 'url_print_status', 'url_bdo_planner', 'siege', 'node_seg',
                  'node_ter', 'node_qua', 'node_qui', 'node_sex', 'node_dom', 'ativo', 'cargo']
        labels = {
            'user_discord': 'ID Discord',
            'nome_familia': 'Nome da Família',
            'nome_char_principal': 'Char Principal',
            'char_lvl': 'Level',
            'char_classe': 'Classe',
            'char_ap': 'PA',
            'char_ap_despertada': 'PA Despertado',
            'char_dp': 'PD',
            'gs': 'GS',
            'url_print_status': 'Print da Tela Inteira do jogo com seu PA e PD',
            'url_bdo_planner': 'URL da sua Build Atual no BDO Planner',
            'siege': 'Disponível para participar de Siege aos Sábados'
        }
        widgets = {
            'user_discord': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome_familia': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome_char_principal': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'char_lvl': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_classe': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'char_ap': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_ap_despertada': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'char_dp': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'number'}),
            'gs': forms.TextInput(attrs={'class': 'form-control font-bold text-primary', 'required': True,
                                         'type': 'number', 'readonly': True}),
            'url_print_status': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'url_bdo_planner': forms.TextInput(attrs={'class': 'form-control'}),
            'siege': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }
