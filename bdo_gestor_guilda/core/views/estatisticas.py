from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json

from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from datetime import date


@login_required
def index(request):
    hoje = date.today()
    grafico_guerra_dia = []
    context = utils.get_context(request)
    ultimas_7_guerras = Guerras.objects.all().exclude(data_inicio=hoje).order_by('-data_inicio')[:7]
    ultimas_7_guerras = reversed(ultimas_7_guerras)
    for guerra in ultimas_7_guerras:
        participacoes = ParticiparGuerra.objects.filter(
            guerra=guerra, participa=ParticiparGuerra.PARTICIPAR_SIM).exclude(
            participante__cargo=UserAvancado.CARGO_HEROI_ID).count()
        frequencias = FrequenciaGuerra.objects.filter(guerra=guerra).first()
        if frequencias and frequencias.participantes:
            frequencias = frequencias.participantes.__len__()
        else:
            frequencias = 0
        grafico_guerra_dia.append({
            'dia': '{}/{}/{}'.format(guerra.data_inicio.day, guerra.data_inicio.month, guerra.data_inicio.year),
            'participacoes': participacoes, 'frequencias': frequencias})

    json_grafico_guerra_dia = json.dumps(grafico_guerra_dia)
    context.update({'json_grafico_guerra_dia': json_grafico_guerra_dia})
    return render(request, '{0}/index.html'.format(utils.path_estatisticas), context)
