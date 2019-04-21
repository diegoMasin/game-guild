from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes

# URLS
url_name_login = 'usuario_login'
url_name_logout = 'usuario_logout'
url_name_signup = 'usuario_signup'
url_name_termo = 'usuario_termo'
url_name_cadastrar_user_avancado = 'cadastrar_user_avancado'
url_name_inserir_user_avancado = 'inserir_user_avancado'
url_name_aguarde_aprovacao = 'usuario_aguarde_aprovacao'
url_name_home = 'pagina_inicial'
# PATHS
path_template_login = 'login'
path_template_home = 'pagina_inicial'
path_user_avancado = 'user_avancado'
# CONTEXT
context = {
    'url_name_login': url_name_login,
    'url_name_logout': url_name_logout,
    'url_name_signup': url_name_signup,
    'url_name_termo': url_name_termo,
    'url_name_user_avancado': url_name_cadastrar_user_avancado,
    'url_name_inserir_user_avancado': url_name_inserir_user_avancado,
    'url_name_aguarde_aprovacao': url_name_aguarde_aprovacao,
    'url_name_home': url_name_home,

    'path_template_login': path_template_login,
    'path_template_home': path_template_home,
    'path_user_avancado': path_user_avancado
}


def get_context(requisicao=None):
    if requisicao:
        context.update({'nome_usuario': requisicao.user.first_name})
    return context


def remove_moeda(string):
    if not string:
        return None

    string = str(string)
    string = string.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')

    return Decimal(string)


@login_required
def set_usuario_owner(request, data):
    from django import forms

    try:
        if isinstance(data, forms.ModelForm) or isinstance(data, forms.Form):
            data = data.cleaned_data

        usuario_logado = request.user
        data['usuario'] = usuario_logado

    except ValueError:
        messages.warning(request, TextosPadroes.usuario_nao_logado())

    return data
