from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.configuracoes import Configuracoes
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
from bdo_gestor_guilda.core.models.payout import Payout
from bdo_gestor_guilda.core.models.payout_personalizado import PayoutPersonalizado
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar
from bdo_gestor_guilda.usuario.forms.tipo_classe_char import TipoClasseCharForm
from bdo_gestor_guilda.core.models.termo_condicoes import TermoCondicoes


@login_required
def index(request):
    context = utils.get_context(request)
    if context.get('dados_avancados').is_lider():
        num_registros, percent = utils.contador_de_registros()
        todas_configuracoes = Configuracoes.objects.all().order_by('pk')

        context.update({'todas_configuracoes': todas_configuracoes})
        context.update({'num_registros': num_registros})
        context.update({'percent': percent})
        return render(request, '{0}/index.html'.format(utils.path_configuracoes), context)
    return redirect(utils.url_name_home)


@login_required
def atualizar(request, conf_id):
    try:
        if request.method == 'POST':
            conf = Configuracoes.objects.get(pk=conf_id)
            esta_valido, mensagem = validacao_geral(conf)
            if esta_valido:
                valor = request.POST.get('valor_conf')
                if conf.tipo_variavel == conf.STRING_ID:
                    conf.valor_string = valor
                    if 'http' not in valor and conf.nome_variavel == Configuracoes.NOME_VARIAVEL_SITE_GUILDA:
                        conf.valor_string = '{0}{1}'.format('https://', valor)
                elif conf.tipo_variavel == conf.INTEIRO_ID:
                    conf.valor_inteiro = valor
                elif conf.tipo_variavel == conf.BOOL_ID:
                    conf.valor_bool = valor
                conf.save()
                messages.success(request, 'A variável ({}) foi atualizada com Sucesso!'.format(conf.slug_variavel))
            else:
                messages.warning(request, mensagem)
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(reverse(utils.url_configuracoes_index))


def validacao_geral(conf):
    validado = True
    mensagem = ''
    return validado, mensagem


@login_required
def limpar_registros(request):
    from datetime import date, datetime
    from monthdelta import monthdelta
    try:
        with transaction.atomic():
            if request.method == 'POST':
                meses = int(request.POST.get('meses_limpar'))
                data_limpeza = date.today() - monthdelta(meses)
                guerras_limpeza = Guerras.objects.filter(data_inicio__lte=data_limpeza)
                participacoes_limpeza = ParticiparGuerra.objects.filter(guerra__in=guerras_limpeza)
                frequencias_limpeza = FrequenciaGuerra.objects.filter(guerra__in=guerras_limpeza)
                payout_limpeza = Payout.objects.filter(data_inicio__lte=data_limpeza)
                payout_personalizado_limpeza = PayoutPersonalizado.objects.filter(payout__in=payout_limpeza)
                convert_datetime = datetime.combine(data_limpeza, datetime.max.time())
                black_list_limpeza = UserAvancado.objects.filter(ativo=False, cargo=UserAvancado.CARGO_NENHUM_ID,
                                                                 data_cadastro__lte=convert_datetime)

                contador = guerras_limpeza.count() + participacoes_limpeza.count() + frequencias_limpeza.count()
                contador = contador + payout_limpeza.count() + payout_personalizado_limpeza.count()
                contador = contador + black_list_limpeza.count()

                participacoes_limpeza.delete()
                frequencias_limpeza.delete()
                guerras_limpeza.delete()
                payout_personalizado_limpeza.delete()
                payout_limpeza.delete()
                black_list_limpeza.delete()
                if contador == 0:
                    messages.warning(request, 'Não havia registros a serem apagados.')
                else:
                    messages.success(request, '{} registros foram apagados.'.format(contador))
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
        transaction.rollback()
    else:
        transaction.commit()
    return redirect(utils.url_configuracoes_index)


@login_required
def termo_condicoes(request):
    context = utils.get_context(request)
    if context.get('dados_avancados').is_lider():
        termo = TermoCondicoes.objects.all().last()
        context.update({'termo': termo})
        if request.method == 'POST':
            try:
                termo.texto = request.POST.get('termo_condicoes')
                termo.save()
                messages.success(request, 'O texto de Termo e Condições foi Atualizado com Sucesso!')
            except Exception as e:
                messages.warning(request, TextosPadroes.erro_padrao())
        return render(request, '{0}/termo_condicoes.html'.format(utils.path_configuracoes), context)
    return redirect(utils.url_configuracoes_index)


@login_required
def tipo_classe_char_listar(request):
    context = utils.get_context(request)
    if context.get('dados_avancados').is_lider():
        all_classes = TipoClasseChar.objects.all().order_by('slug')

        context.update({'all_classes': all_classes})
        return render(request, '{0}/tipo_classe_char_listar.html'.format(utils.path_configuracoes), context)
    return redirect(utils.url_configuracoes_index)


@login_required
def tipo_classe_char_editar(request, tipo_classe_id):
    try:
        classe = TipoClasseChar.objects.get(pk=tipo_classe_id)
        context = utils.get_context(request)
        context.update({'form': TipoClasseCharForm(instance=classe)})
        context.update({'classe': classe})
    except Exception as e:
        messages.error(request, TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_configuracoes_tipo_classe_char_listar))
    return render(request, '{0}/tipo_classe_char_editar.html'.format(utils.path_configuracoes), context)
