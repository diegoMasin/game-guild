import random
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
url_reset_senha = 'password_reset'
url_name_cadastrar_user_avancado = 'cadastrar_user_avancado'
url_name_inserir_user_avancado = 'inserir_user_avancado'
url_name_aguarde_aprovacao = 'usuario_aguarde_aprovacao'
url_usuario_editar_perfil = 'usuario_editar_perfil'
url_usuario_atualizar_perfil = 'usuario_atualizar_perfil'
url_name_home = 'pagina_inicial'
url_inserir_participante_guerra = 'inserir_participante_guerra'
url_recrutas_listar = 'recrutas_listar'
url_recrutas_recrutar_ativar = 'recrutas_recrutar_ativar'
url_recrutar_reprovar = 'recrutar_reprovar'
url_membros_listar = 'membros_listar'
url_membros_promover = 'membros_promover'
url_membros_rebaixar = 'membros_rebaixar'
url_membros_inativar = 'membros_inativar'
url_grupos_listar = 'grupos_listar'
url_grupos_cadastrar = 'grupos_cadastrar'
url_grupos_inserir = 'grupos_inserir'
url_grupos_editar = 'grupos_editar'
url_grupos_atualizar = 'grupos_atualizar'
url_grupos_deletar = 'grupos_deletar'
url_vinculo_grupos_cadastrar = 'vinculo_grupos_cadastrar'
url_vinculo_grupos_inserir = 'vinculo_grupos_inserir'
url_vinculo_grupos_deletar = 'vinculo_grupos_deletar'
url_anuncios_gerais_cadastrar = 'anuncios_gerais_cadastrar'
url_anuncios_gerais_inserir = 'anuncios_gerais_inserir'
url_anuncios_gerais_deletar = 'anuncios_gerais_deletar'
url_anuncios_restritos_cadastrar = 'anuncios_restritos_cadastrar'
url_anuncios_restritos_inserir = 'anuncios_restritos_inserir'
url_anuncios_restritos_deletar = 'anuncios_restritos_deletar'
url_guerras_listar = 'guerras_listar'
url_guerras_cadastrar = 'guerras_cadastrar'
url_guerras_inserir = 'guerras_inserir'
url_guerras_editar = 'guerras_editar'
url_guerras_atualizar = 'guerras_atualizar'
url_guerras_excluir = 'guerras_excluir'
url_lista_negra_listar = 'lista_negra_listar'
url_lista_negra_reativar = 'lista_negra_reativar'
url_frequencia_guerra_listar = 'frequencia_guerra_listar'
url_frequencia_guerra_marcar = 'frequencia_guerra_marcar'
# PATHS
path_template_login = 'login'
path_template_home = 'pagina_inicial'
path_user_avancado = 'user_avancado'
path_recover = 'recover'
path_recrutas = 'recrutas'
path_membros = 'membros'
path_lista_negra = 'lista_negra'
path_grupos = 'grupos'
path_vinculo_grupos = 'vinculo_grupos'
path_anuncios_gerais = 'anuncios_gerais'
path_anuncios_restritos = 'anuncios_restritos'
path_guerras = 'guerras'
# CONTEXT
context = {
    'url_name_login': url_name_login,
    'url_name_logout': url_name_logout,
    'url_name_signup': url_name_signup,
    'url_name_termo': url_name_termo,
    'url_reset_senha': url_reset_senha,
    'url_name_user_avancado': url_name_cadastrar_user_avancado,
    'url_name_inserir_user_avancado': url_name_inserir_user_avancado,
    'url_name_aguarde_aprovacao': url_name_aguarde_aprovacao,
    'url_usuario_editar_perfil': url_usuario_editar_perfil,
    'url_usuario_atualizar_perfil': url_usuario_atualizar_perfil,
    'url_name_home': url_name_home,
    'url_inserir_participante_guerra': url_inserir_participante_guerra,
    'url_recrutas_listar': url_recrutas_listar,
    'url_recrutas_recrutar_ativar': url_recrutas_recrutar_ativar,
    'url_recrutar_reprovar': url_recrutar_reprovar,
    'url_membros_listar': url_membros_listar,
    'url_membros_promover': url_membros_promover,
    'url_membros_rebaixar': url_membros_rebaixar,
    'url_membros_inativar': url_membros_inativar,
    'url_grupos_listar': url_grupos_listar,
    'url_grupos_cadastrar': url_grupos_cadastrar,
    'url_grupos_inserir': url_grupos_inserir,
    'url_grupos_editar': url_grupos_editar,
    'url_grupos_atualizar': url_grupos_atualizar,
    'url_grupos_deletar': url_grupos_deletar,
    'url_vinculo_grupos_cadastrar': url_vinculo_grupos_cadastrar,
    'url_vinculo_grupos_inserir': url_vinculo_grupos_inserir,
    'url_vinculo_grupos_deletar': url_vinculo_grupos_deletar,
    'url_anuncios_gerais_cadastrar': url_anuncios_gerais_cadastrar,
    'url_anuncios_gerais_inserir': url_anuncios_gerais_inserir,
    'url_anuncios_gerais_deletar': url_anuncios_gerais_deletar,
    'url_anuncios_restritos_cadastrar': url_anuncios_restritos_cadastrar,
    'url_anuncios_restritos_inserir': url_anuncios_restritos_inserir,
    'url_anuncios_restritos_deletar': url_anuncios_restritos_deletar,
    'url_guerras_listar': url_guerras_listar,
    'url_guerras_cadastrar': url_guerras_cadastrar,
    'url_guerras_inserir': url_guerras_inserir,
    'url_guerras_editar': url_guerras_editar,
    'url_guerras_atualizar': url_guerras_atualizar,
    'url_guerras_excluir': url_guerras_excluir,
    'url_lista_negra_listar': url_lista_negra_listar,
    'url_lista_negra_reativar': url_lista_negra_reativar,
    'url_frequencia_guerra_listar': url_frequencia_guerra_listar,
    'url_frequencia_guerra_marcar': url_frequencia_guerra_marcar,

    'path_template_login': path_template_login,
    'path_template_home': path_template_home,
    'path_user_avancado': path_user_avancado,
    'path_recover': path_recover
}


def get_context(requisicao=None):
    if requisicao:
        dados_avancados = UserAvancado.objects.filter(usuario=requisicao.user).first()
        if dados_avancados:
            nome_classe = dados_avancados.char_classe.nome_classe
            context.update({'logo_pequena': 'v1/global/assets/images/logo_classes/{0}.png'.format(nome_classe)})
            context.update({'foto_classe': 'v1/global/assets/images/foto_classes/{0}.png'.format(nome_classe)})
            context.update({'escolha_random': bool(random.getrandbits(1))})

            context.update({'dados_avancados': dados_avancados})
            context.update({'id_user_avancado': dados_avancados.pk})
            context.update({'familia': dados_avancados.nome_familia})
            context.update({'char': dados_avancados.nome_char_principal})
            context.update({'discord': dados_avancados.user_discord})
            context.update({'level': dados_avancados.char_lvl})
            context.update({'gs': dados_avancados.gs})
            context.update({'cargo': dados_avancados.cargo})
            context.update({'classe': dados_avancados.char_classe})
            context.update({'is_lider_or_oficial': dados_avancados.is_lider_or_oficial()})
            context.update({'is_lider': dados_avancados.is_lider()})

            context.update({'pt_fixa': dados_avancados.get_pt_fixa()})

        context.update({'nome_usuario': requisicao.user.first_name})
        context.update({'id_usuario': requisicao.user.pk})
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


def render_com_form_preenchido(requisicao, path, html, form):
    contexts = get_context(requisicao)
    contexts.update({'form': form})
    return '{}/{}'.format(path, html), contexts


def pode_promover_ou_rebaixar(request):
    from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
    dados_avancados = UserAvancado.objects.filter(usuario=request.user, cargo=UserAvancado.CARGO_LIDER_ID)
    return True if dados_avancados else False
