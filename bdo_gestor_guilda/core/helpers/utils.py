import random
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos

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
url_recrutar_reprovar = 'recrutar_reprovar'
url_membros_listar = 'membros_listar'
url_membros_promover = 'membros_promover'
url_membros_rebaixar = 'membros_rebaixar'
url_grupos_listar = 'grupos_listar'
url_grupos_cadastrar = 'grupos_cadastrar'
url_grupos_inserir = 'grupos_inserir'
url_grupos_deletar = 'grupos_deletar'
url_vinculo_grupos_cadastrar = 'vinculo_grupos_cadastrar'
url_vinculo_grupos_inserir = 'vinculo_grupos_inserir'
# PATHS
path_template_login = 'login'
path_template_home = 'pagina_inicial'
path_user_avancado = 'user_avancado'
path_recrutas = 'recrutas'
path_membros = 'membros'
path_grupos = 'grupos'
path_vinculo_grupos = 'vinculo_grupos'
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
    'url_recrutar_reprovar': url_recrutar_reprovar,
    'url_membros_listar': url_membros_listar,
    'url_membros_promover': url_membros_promover,
    'url_membros_rebaixar': url_membros_rebaixar,
    'url_grupos_listar': url_grupos_listar,
    'url_grupos_cadastrar': url_grupos_cadastrar,
    'url_grupos_inserir': url_grupos_inserir,
    'url_grupos_deletar': url_grupos_deletar,
    'url_vinculo_grupos_cadastrar': url_vinculo_grupos_cadastrar,
    'url_vinculo_grupos_inserir': url_vinculo_grupos_inserir,

    'path_template_login': path_template_login,
    'path_template_home': path_template_home,
    'path_user_avancado': path_user_avancado
}


def get_context(requisicao=None):
    if requisicao:
        dados_avancados = UserAvancado.objects.filter(usuario=requisicao.user).first()
        if dados_avancados:
            context.update({'familia': dados_avancados.nome_familia})
            nome_classe = dados_avancados.char_classe.nome_classe
            context.update({'logo_pequena': 'v1/global/assets/images/logo_classes/{0}.png'.format(nome_classe)})
            context.update({'foto_classe': 'v1/global/assets/images/foto_classes/{0}.png'.format(nome_classe)})
            context.update({'escolha_random': bool(random.getrandbits(1))})

            context.update({'familia': dados_avancados.nome_familia})
            context.update({'char': dados_avancados.nome_char_principal})
            context.update({'discord': dados_avancados.user_discord})
            context.update({'level': dados_avancados.char_lvl})
            context.update({'gs': dados_avancados.gs})
            context.update({'cargo': dados_avancados.cargo})
            context.update({'classe': dados_avancados.char_classe})
            context.update({'is_lider_or_oficial': dados_avancados.is_lider_or_oficial()})
            context.update({'is_lider': dados_avancados.is_lider()})

            context.update({'pt_fixa': get_pt_fixa(dados_avancados)})

        context.update({'nome_usuario': requisicao.user.first_name})
        context.update({'id_usuario': requisicao.user.pk})
    return context


def get_pt_fixa(user_dados_avancados):
    pt_fixa = ''
    lider_user_logado = Grupos.objects.filter(lider=user_dados_avancados).first()
    membro_user_logado = VinculoGrupos.objects.filter(membro=user_dados_avancados).first()
    if lider_user_logado:
        pt_fixa = 'Líder do(a) {}'.format(lider_user_logado)
    if membro_user_logado:
        pt_fixa = 'Membro do(a) {}'.format(membro_user_logado.grupo)
    return pt_fixa


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


def render_com_form_preenchido(requisicao, path, html, form):
    contexts = get_context(requisicao)
    contexts.update({'form': form})
    return '{}/{}'.format(path, html), contexts


def pode_promover_ou_rebaixar(request):
    from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
    dados_avancados = UserAvancado.objects.filter(usuario=request.user, cargo=UserAvancado.CARGO_LIDER_ID)
    return True if dados_avancados else False
