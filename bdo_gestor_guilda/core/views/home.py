from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.forms.participar_guerra import ParticiparGuerraForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.anuncios_gerais import AnunciosGerais
from bdo_gestor_guilda.core.models.anuncios_restrito import AnunciosRestritos
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
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

    anuncio_geral = AnunciosGerais.objects.last()
    anuncio_restrito = AnunciosRestritos.objects.last()
    guerra_de_hoje = Guerras.objects.filter(data_inicio=date.today()).first()
    logado_participa_guerra = ParticiparGuerra.objects.filter(guerra=guerra_de_hoje).first()

    context.update({'anuncio_geral': anuncio_geral})
    context.update({'anuncio_restrito': anuncio_restrito})
    context.update({'guerra_de_hoje': guerra_de_hoje})
    context.update({'logado_participa_guerra': logado_participa_guerra})
    context.update({'form_participa': ParticiparGuerraForm(initial={'guerra': guerra_de_hoje,
                                                                    'participante': dados_user_avancado.first()})})
    return render(request, '{0}/index.html'.format(utils.path_template_home), context)


@login_required
def inserir_participante_guerra(request):
    try:
        if request.method == 'POST':
            form = ParticiparGuerraForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                participacao = ParticiparGuerra.objects.filter(guerra=dados.get('guerra'),
                                                               participante=dados.get('participante')).first()
                if participacao:
                    participacao.delete()
                ParticiparGuerra(**dados).save()
                messages.success(request, 'Sua participação foi realizada com Sucesso.')
                return redirect(utils.url_name_home)
            else:
                erros_form = TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
    return redirect(utils.url_name_home)
