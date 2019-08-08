from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def listar(request):
    context = utils.get_context(request)
    todos_usuarios_inativos = UserAvancado.objects.filter(ativo=False).exclude(
        justificativa_inativo__isnull=True).exclude(justificativa_inativo__exact='').order_by('cargo')
    context.update({'todos_usuarios_inativos': todos_usuarios_inativos})
    return render(request, '{0}/index.html'.format(utils.path_lista_negra), context)


@login_required
def reativar(request, user_avancado_id):
    try:
        with transaction.atomic():
            context = utils.get_context(request)
            if context.get('is_lider'):
                user_avancado = UserAvancado.objects.filter(pk=user_avancado_id).first()
                user_avancado.ativo = True
                user_avancado.cargo = UserAvancado.CARGO_MEMBRO_ID
                user_avancado.justificativa_inativo = None
                user_avancado.save()
                user = User.objects.filter(pk=user_avancado.usuario.pk).first()
                user.is_active = True
                user.save()
                messages.success(request, 'Membro Reativado na Guilda com Sucesso!')
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        transaction.rollback()
    else:
        transaction.commit()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def reativar_heroi(request, user_avancado_id):
    try:
        with transaction.atomic():
            context = utils.get_context(request)
            if context.get('is_lider'):
                user_avancado = UserAvancado.objects.filter(pk=user_avancado_id).first()
                user_avancado.ativo = True
                user_avancado.cargo = UserAvancado.CARGO_HEROI_ID
                user_avancado.justificativa_inativo = None
                user_avancado.save()
                user = User.objects.filter(pk=user_avancado.usuario.pk).first()
                user.is_active = True
                user.save()
                messages.success(request, 'Herói Reativado na Guilda com Sucesso!')
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        transaction.rollback()
    else:
        transaction.commit()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
