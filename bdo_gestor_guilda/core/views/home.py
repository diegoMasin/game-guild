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
    context.update({'guerra_de_hoje': guerra_de_hoje})
    if guerra_de_hoje:
        logado_participa_guerra = ParticiparGuerra.objects.filter(
            guerra=guerra_de_hoje, participante=dados_user_avancado.first()).first()
        total_guerra_hoje = ParticiparGuerra.objects.filter(guerra=guerra_de_hoje)
        total_sim_guerra_hoje = total_guerra_hoje.filter(participa=ParticiparGuerra.PARTICIPAR_SIM)
        total_nao_guerra_hoje = total_guerra_hoje.filter(participa=ParticiparGuerra.PARTICIPAR_NAO)
        total_talvez_guerra_hoje = total_guerra_hoje.filter(participa=ParticiparGuerra.PARTICIPAR_TALVEZ)
        context.update({'total_guerra_hoje': total_guerra_hoje.count()})
        context.update({'total_sim_guerra_hoje': total_sim_guerra_hoje.count()})
        context.update({'total_nao_guerra_hoje': total_nao_guerra_hoje.count()})
        context.update({'total_talvez_guerra_hoje': total_talvez_guerra_hoje.count()})
        context.update({'logado_participa_guerra': logado_participa_guerra})

    siege_da_semana = Guerras.objects.filter(
        tipo=Guerras.TIPO_SIEGE_ID, data_inicio__gte=date.today()).order_by('data_inicio').first()
    context.update({'siege_da_semana': siege_da_semana})
    if siege_da_semana:
        logado_participa_siege_semana = ParticiparGuerra.objects.filter(
            guerra=siege_da_semana, participante=dados_user_avancado.first()).first()
        total_siege_semana = ParticiparGuerra.objects.filter(guerra=siege_da_semana)
        total_sim_siege_semana = total_siege_semana.filter(participa=ParticiparGuerra.PARTICIPAR_SIM)
        total_nao_siege_semana = total_siege_semana.filter(participa=ParticiparGuerra.PARTICIPAR_NAO)
        total_talvez_siege_semana = total_siege_semana.filter(participa=ParticiparGuerra.PARTICIPAR_TALVEZ)
        context.update({'total_siege_semana': total_siege_semana.count()})
        context.update({'total_sim_siege_semana': total_sim_siege_semana.count()})
        context.update({'total_nao_siege_semana': total_nao_siege_semana.count()})
        context.update({'total_talvez_siege_semana': total_talvez_siege_semana.count()})
        context.update({'logado_participa_siege_semana': logado_participa_siege_semana})
        context.update({'form_participa_siege_semana': ParticiparGuerraForm(initial={
            'guerra': siege_da_semana, 'participante': dados_user_avancado.first()})})

    context.update({'anuncio_geral': anuncio_geral})
    context.update({'anuncio_restrito': anuncio_restrito})
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
                is_guerra_de_hoje = Guerras.objects.filter(data_inicio=date.today()).first() == dados.get('guerra')
                if is_guerra_de_hoje:
                    if not utils.passou_das_21hr():
                        if participacao:
                            participacao.delete()
                        ParticiparGuerra(**dados).save()
                        messages.success(request, 'Sua participação foi realizada com Sucesso.')
                    else:
                        messages.warning(request, 'Passou do horário de Registrar a Participação na Guerra.')
                else:
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
