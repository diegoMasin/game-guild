from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.anuncios_gerais import AnunciosGerais
from bdo_gestor_guilda.core.models.anuncios_restrito import AnunciosRestritos
from bdo_gestor_guilda.core.models.guerras import Guerras


@login_required
def pagina_inicial(request):
    context = utils.get_context(request)

    dados_user_avancado = UserAvancado.objects.filter(usuario=request.user)
    if not dados_user_avancado:
        return redirect(utils.url_name_cadastrar_user_avancado)
    else:
        if not dados_user_avancado.first().ativo:
            return redirect(utils.url_name_aguarde_aprovacao)

    anuncio_geral = AnunciosGerais.objects.last()
    anuncio_restrito = AnunciosRestritos.objects.last()
    guerra_de_hoje = Guerras.objects.filter(data_inicio=date.today()).first()
    context.update({'anuncio_geral': anuncio_geral})
    context.update({'anuncio_restrito': anuncio_restrito})
    context.update({'guerra_de_hoje': guerra_de_hoje})
    return render(request, '{0}/index.html'.format(utils.path_template_home), context)
