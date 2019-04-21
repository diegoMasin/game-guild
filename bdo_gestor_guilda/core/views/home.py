from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def pagina_inicial(request):
    context = utils.get_context(request)
    dados_user_avancado = UserAvancado.objects.filter(usuario=request.user)
    if not dados_user_avancado:
        return redirect(utils.url_name_cadastrar_user_avancado)
    else:
        if not dados_user_avancado.first().ativo:
            return redirect(utils.url_name_aguarde_aprovacao)
    return render(request, '{0}/index.html'.format(utils.path_template_home), context)
