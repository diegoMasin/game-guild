from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.forms.payout import PayoutForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.payout import Payout
from bdo_gestor_guilda.core.models.payout_personalizado import PayoutPersonalizado
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


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


@login_required
def listar_calculos(request, payout_id):
    context = utils.get_context(request)
    todos_membros_ativos = UserAvancado.objects.filter(ativo=True).order_by('cargo')
    payout = Payout.objects.filter(pk=int(payout_id)).first()

    total_guerras_by_payout = Guerras.objects.filter(data_inicio__range=[payout.data_inicio, payout.data_fim])
    total_de_nodes_by_payout = total_guerras_by_payout.filter(tipo=Guerras.TIPO_NODEWAR_ID)
    total_de_siege_by_payout = total_guerras_by_payout.filter(tipo=Guerras.TIPO_SIEGE_ID)
    tier_adicional = PayoutPersonalizado.objects.filter(payout=payout)

    context.update({'payout': payout})
    context.update({'todos_membros_ativos': todos_membros_ativos})
    context.update({'total_de_nodes_by_payout': total_de_nodes_by_payout})
    context.update({'total_de_siege_by_payout': total_de_siege_by_payout})
    # url_marcar = reverse(utils.url_frequencia_guerra_marcar)
    # context.update({'url_marcar': url_marcar})
    return render(request, '{0}/calculadora_payout.html'.format(utils.path_payout), context)


@login_required
def adicionar_tier(request):
    try:
        payout = Payout.objects.get(pk=int(request.POST.get('payout_id')))
        membro = UserAvancado.objects.get(pk=int(request.POST.get('membro_id')))
        tier_adicional = int(request.POST.get('tier_adicional'))
        tem_tier_adicional = PayoutPersonalizado.objects.filter(payout=payout, usuario=membro).first()
        if tier_adicional < 0:
            messages.error(request, 'Não é permitido colocar valor negativo.')
        else:
            if tem_tier_adicional:
                tem_tier_adicional.tier_adicional = tier_adicional
                tem_tier_adicional.save()
                messages.success(request, 'Tier Adicionado com Sucesso para {}!'.format(membro.nome_familia))
            else:
                dados = {'payout': payout, 'usuario': membro, 'tier_adicional': tier_adicional}
                PayoutPersonalizado(**dados).save()
                messages.success(request, 'Tier Adicionado com Sucesso para {}!'.format(membro.nome_familia))
    except Exception as e:
        messages.error(request, TextosPadroes.erro_padrao())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
