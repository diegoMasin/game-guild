from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def listar(request):
    context = utils.get_context(request)
    todos_usuarios = UserAvancado.objects.filter(ativo=True).exclude(cargo=UserAvancado.CARGO_HEROI_ID).order_by('cargo')
    context.update({'todos_usuarios': todos_usuarios})
    context.update({'pode_promover_ou_rebaixar': utils.pode_promover_ou_rebaixar(request)})
    return render(request, '{0}/index.html'.format(utils.path_membros), context)


@login_required
def promover(request, user_avancado_id):
    try:
        context = utils.get_context(request)
        user = UserAvancado.objects.filter(pk=user_avancado_id).first()
        if user:
            if user.cargo == UserAvancado.CARGO_MEMBRO_ID:
                user.cargo = UserAvancado.CARGO_OFICIAL_ID
            elif user.cargo == UserAvancado.CARGO_OFICIAL_ID:
                user.cargo = UserAvancado.CARGO_LIDER_ID
            user.save()
            messages.success(request, '{0} Promovido com Sucesso!'.format(user))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def rebaixar(request, user_avancado_id):
    try:
        context = utils.get_context(request)
        user = UserAvancado.objects.filter(pk=user_avancado_id).first()
        if user:
            if user.cargo == UserAvancado.CARGO_LIDER_ID:
                user.cargo = UserAvancado.CARGO_OFICIAL_ID
            elif user.cargo == UserAvancado.CARGO_OFICIAL_ID:
                user.cargo = UserAvancado.CARGO_MEMBRO_ID
            user.save()
            messages.success(request, '{0} Rebaixado com Sucesso!'.format(user))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def inativar(request):
    try:
        with transaction.atomic():
            context = utils.get_context(request)
            id_user_avancado = request.POST.get('id_user_avancado')
            justificativa = request.POST.get('justificativa_inativacao')
            if context.get('is_lider'):
                user_avancado = UserAvancado.objects.filter(pk=id_user_avancado).first()
                is_user_lider_pt_fixa = Grupos.objects.filter(lider=user_avancado).first()
                is_user_membro_pt_fixa = VinculoGrupos.objects.filter(membro=user_avancado).first()
                if is_user_lider_pt_fixa:
                    messages.error(request, '{} é Líder de uma PT Fixa. Remova-o da PT!'.format(user_avancado))
                elif is_user_membro_pt_fixa:
                    messages.error(request, '{} é Membro de uma PT Fixa. Remova-o da PT!'.format(user_avancado))
                else:
                    nome_cargo = user_avancado.get_slug_cargo()
                    user_avancado.ativo = False
                    user_avancado.cargo = UserAvancado.CARGO_NENHUM_ID
                    user_avancado.justificativa_inativo = justificativa
                    user_avancado.save()
                    user = User.objects.filter(pk=user_avancado.usuario.pk).first()
                    user.is_active = False
                    user.save()
                    messages.success(request, '{} Inativado com Sucesso! Movido para a Lista Negra.'.format(nome_cargo))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        transaction.rollback()
    else:
        transaction.commit()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tornar_heroi(request, user_avancado_id):
    try:
        context = utils.get_context(request)
        user = UserAvancado.objects.filter(pk=user_avancado_id).first()
        if user and context.get('is_lider'):
            if user.cargo == UserAvancado.CARGO_MEMBRO_ID:
                user.cargo = UserAvancado.CARGO_HEROI_ID
                user.save()
                messages.success(request, '{0} agora é um Herói da Guilda!'.format(user))
            else:
                messages.warning(request, 'Você deve rebaixe {} a Membro primeiramente'.format(user))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def listar_herois(request):
    context = utils.get_context(request)
    todos_usuarios = UserAvancado.objects.filter(ativo=True, cargo=UserAvancado.CARGO_HEROI_ID).order_by('cargo')
    context.update({'todos_usuarios': todos_usuarios})
    return render(request, '{0}/index.html'.format(utils.path_herois), context)


@login_required
def tornar_membro(request, user_avancado_id):
    try:
        context = utils.get_context(request)
        user = UserAvancado.objects.filter(pk=user_avancado_id).first()
        if user and context.get('is_lider'):
            user.cargo = UserAvancado.CARGO_MEMBRO_ID
            user.save()
            messages.success(request, '{0} agora é um Membro da Guilda!'.format(user))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
