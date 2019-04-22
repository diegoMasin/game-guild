from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def listar(request):
    context = utils.get_context(request)
    todos_usuarios = UserAvancado.objects.filter(ativo=False).order_by('-data_cadastro')
    context.update({'todos_usuarios': todos_usuarios})
    return render(request, '{0}/index.html'.format(utils.path_recrutas), context)
