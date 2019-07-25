from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.forms.guerras import GuerrasForm
from bdo_gestor_guilda.core.forms.payout import PayoutForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.payout import Payout
from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra


@login_required
def listar(request):
    context = utils.get_context(request)
    payouts = Payout.objects.all()
    context.update({'payouts': payouts})
    return render(request, '{0}/index.html'.format(utils.path_payout), context)


@login_required
def cadastrar(request):
    form = PayoutForm()
    context = utils.get_context(request)
    context.update({'form': form})
    return render(request, '{0}/cadastrar.html'.format(utils.path_payout), utils.context)


@login_required
def inserir(request):
    try:
        if request.method == 'POST':
            form = PayoutForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                Payout(**dados).save()
                messages.success(request, TextosPadroes.salvar_sucesso_o('Payout'))
                return redirect(utils.url_payout_listar)
            else:
                erros_form = TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
    return redirect(utils.url_payout_cadastrar)


@login_required
def editar(request, payout_id):
    try:
        payout = Payout.objects.get(pk=payout_id)
        data_inicio = payout.data_inicio
        data_fim = payout.data_fim
        payout.data_inicio = '{}/{}/{}'.format(str(data_inicio.day).zfill(2), str(data_inicio.month).zfill(2),
                                               data_inicio.year)
        payout.data_fim = '{}/{}/{}'.format(str(data_fim.day).zfill(2), str(data_fim.month).zfill(2), data_fim.year)
        context = utils.get_context(request)
        context.update({'form': PayoutForm(instance=payout)})
        context.update({'payout': payout})
    except Exception as e:
        messages.error(request, TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_payout_listar))
    return render(request, '{0}/editar.html'.format(utils.path_payout), context)


@login_required
def atualizar(request, payout_id):
    try:
        if request.method == 'POST':
            payout = Payout.objects.get(pk=payout_id)
            form = PayoutForm(request.POST, instance=payout)
            if form.has_changed():
                if form.is_valid():
                    dados = form.cleaned_data
                    dados['id'] = payout_id
                    Payout(**dados).save()
                    messages.success(request, utils.TextosPadroes.atualizar_sucesso_o('Payout'))
                else:
                    erros_form = utils.TextosPadroes.errors_form(form)
                    for error in erros_form:
                        messages.warning(request, error)
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_payout_listar))
    return HttpResponseRedirect(reverse(utils.url_payout_editar, args=[payout_id]))


@login_required
def excluir(request, payout_id):
    from bdo_gestor_guilda.core.models.payout_personalizado import PayoutPersonalizado
    try:
        with transaction.atomic():
            payout = Payout.objects.get(pk=payout_id)
            payout_personalizado = PayoutPersonalizado.objects.filter(payout=payout)
            if payout_personalizado:
                payout_personalizado.delete()
            payout.delete()
            messages.success(request, TextosPadroes.apagar_sucesso_o('Payout'))
    except Exception as e:
        messages.error(request, TextosPadroes.erro_padrao())
        transaction.rollback()
    else:
        transaction.commit()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required
# def listar(request):
#     context = utils.get_context(request)
#     guerra = Guerras.objects.filter(pk=int(guerra_id)).first()
#     participacoes_guerra = ParticiparGuerra.objects.filter(
#         guerra__pk=int(guerra_id), participa=ParticiparGuerra.PARTICIPAR_SIM).order_by('participante__nome_familia')
#     url_marcar = reverse(utils.url_frequencia_guerra_marcar)
#     context.update({'guerra': guerra})
#     context.update({'participacoes_guerra': participacoes_guerra})
#     context.update({'url_marcar': url_marcar})
#     return render(request, '{0}/marcar_frequencia.html'.format(utils.path_guerras), context)


# @login_required
# def marcar(request):
#     import json
#     from django.http import HttpResponse
#     data = {'sucesso': True}
#     try:
#         if request.method == 'GET':
#             lista_frequencia = []
#             guerra_id = int(request.GET.get('guerra'))
#             user_avancado_id = int(request.GET.get('user_avancado'))
#             tem_frequencia = FrequenciaGuerra.objects.filter(guerra=guerra_id)
#             if tem_frequencia:
#                 frequencia_guerra = tem_frequencia.first()
#                 ja_frequente = tem_frequencia.filter(participantes__contains=[user_avancado_id]).count() > 0
#                 if ja_frequente:
#                     lista_frequencia = frequencia_guerra.participantes
#                     lista_frequencia.remove(user_avancado_id)
#                     frequencia_guerra.participantes = lista_frequencia
#                     frequencia_guerra.save()
#                 else:
#                     lista_frequencia = frequencia_guerra.participantes
#                     lista_frequencia.append(user_avancado_id)
#                     frequencia_guerra.participantes = lista_frequencia
#                     frequencia_guerra.save()
#             else:
#                 lista_frequencia.append(user_avancado_id)
#                 guerra = Guerras.objects.filter(pk=guerra_id).first()
#                 dados = {'guerra': guerra, 'participantes': lista_frequencia}
#                 FrequenciaGuerra(**dados).save()
#     except Exception as e:
#         messages.warning(request, TextosPadroes.erro_padrao())
#     dump = json.dumps(data)
#     return HttpResponse(dump, content_type='application/json')
