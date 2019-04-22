from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado

# URLS
url_name_login = 'usuario_login'
url_name_logout = 'usuario_logout'
url_name_signup = 'usuario_signup'
url_name_termo = 'usuario_termo'
url_name_cadastrar_user_avancado = 'cadastrar_user_avancado'
url_name_inserir_user_avancado = 'inserir_user_avancado'
url_name_aguarde_aprovacao = 'usuario_aguarde_aprovacao'
url_name_home = 'pagina_inicial'
url_recrutas_listar = 'recrutas_listar'
url_recrutas_recrutar_ativar = 'recrutas_recrutar_ativar'
# PATHS
path_template_login = 'login'
path_template_home = 'pagina_inicial'
path_user_avancado = 'user_avancado'
path_recrutas = 'recrutas'
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
    'url_recrutas_listar': url_recrutas_listar,
    'url_recrutas_recrutar_ativar': url_recrutas_recrutar_ativar,

    'path_template_login': path_template_login,
    'path_template_home': path_template_home,
    'path_user_avancado': path_user_avancado
}


def get_context(requisicao=None):
    if requisicao:
        dados_avancados = UserAvancado.objects.filter(usuario=requisicao.user).first()
        if dados_avancados:
            nome_classe = dados_avancados.char_classe.nome_classe
            context.update({'logo_pequena': 'v1/global/assets/images/logo_classes/{0}.png'.format(nome_classe)})
            context.update({'foto_classe': 'v1/global/assets/images/foto_classes/{0}.png'.format(nome_classe)})
            context.update({'familia': dados_avancados.nome_familia})
            context.update({'char': dados_avancados.nome_char_principal})
            context.update({'discord': dados_avancados.user_discord})
            context.update({'level': dados_avancados.char_lvl})
            context.update({'gs': dados_avancados.gs})
            context.update({'classe': nome_classe})
            context.update({'is_lider_or_oficial': dados_avancados.is_lider_or_oficial()})

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
