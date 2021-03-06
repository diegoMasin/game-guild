import random
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.configuracoes import Configuracoes
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado

# URLS
url_name_login = 'usuario_login'
url_name_logout = 'usuario_logout'
url_name_signup = 'usuario_signup'
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
url_recrutas_recrutar_ativar_heroi = 'recrutas_recrutar_ativar_heroi'
url_recrutar_reprovar = 'recrutar_reprovar'
url_membros_listar = 'membros_listar'
url_membros_promover = 'membros_promover'
url_membros_rebaixar = 'membros_rebaixar'
url_membros_inativar = 'membros_inativar'
url_membros_tornar_heroi = 'membros_tornar_heroi'
url_herois_tornar_membro = 'herois_tornar_membro'
url_herois_listar = 'herois_listar'
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
url_lista_negra_reativar_heroi = 'lista_negra_reativar_heroi'
url_frequencia_guerra_listar = 'frequencia_guerra_listar'
url_frequencia_guerra_marcar = 'frequencia_guerra_marcar'
url_payout_listar = 'payout_listar'
url_payout_cadastrar = 'payout_cadastrar'
url_payout_inserir = 'payout_inserir'
url_payout_editar = 'payout_editar'
url_payout_atualizar = 'payout_atualizar'
url_payout_excluir = 'payout_excluir'
url_payout_listar_calculos = 'payout_listar_calculos'
url_payout_adicionar_tier = 'payout_adicionar_tier'
url_configuracoes_index = 'configuracoes_index'
url_configuracoes_atualizar = 'configuracoes_atualizar'
url_configuracoes_limpar_registros = 'configuracoes_limpar_registros'
url_configuracoes_termo_condicoes = 'configuracoes_termo_condicoes'
url_configuracoes_tipo_classe_char_listar = 'configuracoes_tipo_classe_char_listar'
url_configuracoes_tipo_classe_char_editar = 'configuracoes_tipo_classe_char_editar'
url_estatisticas_index = 'estatisticas_index'
# PATHS
path_template_login = 'login'
path_template_home = 'pagina_inicial'
path_user_avancado = 'user_avancado'
path_recover = 'recover'
path_recrutas = 'recrutas'
path_membros = 'membros'
path_herois = 'herois'
path_lista_negra = 'lista_negra'
path_grupos = 'grupos'
path_vinculo_grupos = 'vinculo_grupos'
path_anuncios_gerais = 'anuncios_gerais'
path_anuncios_restritos = 'anuncios_restritos'
path_guerras = 'guerras'
path_payout = 'payout'
path_configuracoes = 'configuracoes'
path_estatisticas = 'estatisticas'
# CONTEXT
context = {
    'url_name_login': url_name_login,
    'url_name_logout': url_name_logout,
    'url_name_signup': url_name_signup,
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
    'url_recrutas_recrutar_ativar_heroi': url_recrutas_recrutar_ativar_heroi,
    'url_recrutar_reprovar': url_recrutar_reprovar,
    'url_membros_listar': url_membros_listar,
    'url_membros_promover': url_membros_promover,
    'url_membros_rebaixar': url_membros_rebaixar,
    'url_membros_inativar': url_membros_inativar,
    'url_membros_tornar_heroi': url_membros_tornar_heroi,
    'url_herois_listar': url_herois_listar,
    'url_herois_tornar_membro': url_herois_tornar_membro,
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
    'url_lista_negra_reativar_heroi': url_lista_negra_reativar_heroi,
    'url_frequencia_guerra_listar': url_frequencia_guerra_listar,
    'url_frequencia_guerra_marcar': url_frequencia_guerra_marcar,
    'url_payout_listar': url_payout_listar,
    'url_payout_cadastrar': url_payout_cadastrar,
    'url_payout_inserir': url_payout_inserir,
    'url_payout_editar': url_payout_editar,
    'url_payout_atualizar': url_payout_atualizar,
    'url_payout_excluir': url_payout_excluir,
    'url_payout_listar_calculos': url_payout_listar_calculos,
    'url_payout_adicionar_tier': url_payout_adicionar_tier,
    'url_configuracoes_index': url_configuracoes_index,
    'url_configuracoes_atualizar': url_configuracoes_atualizar,
    'url_configuracoes_limpar_registros': url_configuracoes_limpar_registros,
    'url_configuracoes_termo_condicoes': url_configuracoes_termo_condicoes,
    'url_configuracoes_tipo_classe_char_listar': url_configuracoes_tipo_classe_char_listar,
    'url_configuracoes_tipo_classe_char_editar': url_configuracoes_tipo_classe_char_editar,
    'url_estatisticas_index': url_estatisticas_index,

    'path_template_login': path_template_login,
    'path_template_home': path_template_home,
    'path_user_avancado': path_user_avancado,
    'path_recover': path_recover,

    'nome_logo': settings.NOME_LOGO,
    'nome_logo_icon': settings.NOME_LOGO_ICON,
    'nome_logo_login': settings.NOME_LOGO_LOGIN,
}


def get_context(requisicao=None):
    if requisicao:
        dados_avancados = UserAvancado.objects.filter(usuario=requisicao.user).first()
        configuracoes = Configuracoes.objects.all()
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
            context.update({'cargo': dados_avancados.get_slug_cargo})
            context.update({'classe': dados_avancados.char_classe})
            context.update({'is_lider_or_oficial': dados_avancados.is_lider_or_oficial()})
            context.update({'is_lider': dados_avancados.is_lider()})
            context.update({'is_oficial': dados_avancados.is_oficial()})
            context.update({'is_heroi': dados_avancados.is_heroi()})
            context.update({'is_membro': dados_avancados.is_membro()})

            context.update({'pt_fixa': dados_avancados.get_pt_fixa()})

        context.update({'nome_usuario': requisicao.user.first_name})
        context.update({'id_usuario': requisicao.user.pk})
        context.update({'passou_da_hora_para_participar_guerra': passou_da_hora_para_participar_guerra(
            configuracoes.filter(nome_variavel='fechamento_war').first().valor_inteiro)})

        context.update({'nome_guilda': configuracoes.filter(nome_variavel='nome_guilda').first().valor_string})
        context.update({'nome_jogo': configuracoes.filter(nome_variavel='nome_jogo').first().valor_string})
        context.update({'cor_topo': configuracoes.filter(nome_variavel='cor_topo').first().valor_string})
        context.update({'cor_lateral': configuracoes.filter(nome_variavel='cor_lateral').first().valor_string})
        context.update({'site_guilda': configuracoes.filter(nome_variavel='site_guilda').first().valor_string})
        context.update({'fechamento_war': configuracoes.filter(nome_variavel='fechamento_war').first().valor_inteiro})
        context.update({'tier_por_node': configuracoes.filter(nome_variavel='tier_por_node').first().valor_inteiro})
        context.update({'tier_por_siege': configuracoes.filter(nome_variavel='tier_por_siege').first().valor_inteiro})
        context.update({'limitacao_membro': configuracoes.filter(
            nome_variavel='limitacao_membro').first().valor_inteiro})
        context.update({'limitacao_heroi': configuracoes.filter(nome_variavel='limitacao_heroi').first().valor_inteiro})
        context.update({'variavel_frequencia_alerta': configuracoes.filter(
            nome_variavel='variavel_frequencia_alerta').first().valor_inteiro})

        context.update({'nome_logo': settings.NOME_LOGO})
        context.update({'nome_logo_icon': settings.NOME_LOGO_ICON})
        context.update({'nome_logo_login': settings.NOME_LOGO_LOGIN})
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


def passou_da_hora_para_participar_guerra(hora):
    from datetime import datetime
    import pytz
    agora = datetime.now(pytz.timezone('Brazil/East'))
    return agora.hour >= hora


def contador_de_registros():
    from bdo_gestor_guilda.core.models.guerras import Guerras
    from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
    from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
    from bdo_gestor_guilda.core.models.payout import Payout
    from bdo_gestor_guilda.core.models.payout_personalizado import PayoutPersonalizado
    from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado

    start_de_seguranca = 1500
    num_registros = start_de_seguranca
    reg_guerras = Guerras.objects.all().count()
    reg_participacoes = ParticiparGuerra.objects.all().count()
    reg_frequencias = FrequenciaGuerra.objects.all().count()
    reg_payout = Payout.objects.all().count()
    reg_payout_personalizado = PayoutPersonalizado.objects.all().count()
    reg_black_list = UserAvancado.objects.filter(ativo=False, cargo=UserAvancado.CARGO_NENHUM_ID).count()

    soma = reg_guerras + reg_participacoes + reg_frequencias + reg_payout + reg_payout_personalizado + reg_black_list
    num_registros = num_registros + soma
    percent = (num_registros * 100) / 10000
    return num_registros, percent


def normaliza_texto(texto):
    from unicodedata import normalize
    result = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return result.lower().replace(' ', '_')


def get_variavel_frequencia_alerta():
    return Configuracoes.objects.filter(nome_variavel='variavel_frequencia_alerta').first().valor_inteiro
