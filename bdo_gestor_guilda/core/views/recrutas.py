from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from django.contrib.auth.models import User
from bdo_gestor_guilda.usuario.models.recruta_reprovado import RecrutaReprovado


@login_required
def listar(request):
    context = utils.get_context(request)
    if context.get('is_lider_or_oficial'):
        todos_usuarios = UserAvancado.objects.filter(ativo=False, justificativa_inativo=None).order_by('-data_cadastro')
        context.update({'todos_usuarios': todos_usuarios})
        return render(request, '{0}/index.html'.format(utils.path_recrutas), context)
    return redirect(utils.url_name_home)


@login_required
def recrutar_ativar(request, user_avancado_id):
    try:
        context = utils.get_context(request)
        if context.get('is_lider_or_oficial'):
            user = UserAvancado.objects.filter(pk=user_avancado_id).first()
            if user:
                user.ativo = True
                user.cargo = UserAvancado.CARGO_MEMBRO_ID
                user.save()
                messages.success(request, '{0} Ativado com Sucesso!'.format(user))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def recrutar_reprovar(request):
    try:
        context = utils.get_context(request)
        id_user_avancado = request.POST.get('id_user_avancado')
        justificativa = request.POST.get('justificativa_reprovacao')
        if context.get('is_lider_or_oficial'):
            user_avancado = UserAvancado.objects.filter(pk=id_user_avancado).first()
            user = User.objects.filter(pk=user_avancado.usuario.pk).first()
            recruta_reprovado = RecrutaReprovado(usuario=user, justificativa=justificativa).save()
            user_avancado.delete()
            messages.success(request, 'Recruta Reprovado com Sucesso!')
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
