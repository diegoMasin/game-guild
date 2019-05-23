from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def listar(request):
    context = utils.get_context(request)
    todos_usuarios = UserAvancado.objects.filter(ativo=True).order_by('cargo')
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
