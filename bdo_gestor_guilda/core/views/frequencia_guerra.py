from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.forms.guerras import GuerrasForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra


@login_required
def listar(request, guerra_id):
    context = utils.get_context(request)
    if context.get('is_lider_or_oficial'):
        guerra = Guerras.objects.filter(pk=int(guerra_id)).first()
        participacoes_guerra = ParticiparGuerra.objects.filter(
            guerra__pk=int(guerra_id), participa=ParticiparGuerra.PARTICIPAR_SIM).order_by('participante__nome_familia')
        context.update({'guerra': guerra})
        context.update({'participacoes_guerra': participacoes_guerra})
        return render(request, '{0}/marcar_frequencia.html'.format(utils.path_guerras), context)
    return redirect(utils.url_guerras_listar)


@login_required
def marcar(request, guerra_id):
    try:
        if request.method == 'POST':
            # FrequenciaGuerra(**dados).save()
            messages.success(request, TextosPadroes.salvar_sucesso_a('Guerra'))
            return redirect(utils.url_guerras_listar)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
    return redirect(utils.url_guerras_cadastrar)
