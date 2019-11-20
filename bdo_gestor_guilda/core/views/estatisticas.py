from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg
import json

from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from datetime import date


@login_required
def index(request):
    all_membros_ativos = UserAvancado.objects.filter(ativo=True).exclude(cargo=UserAvancado.CARGO_HEROI_ID)
    context = utils.get_context(request)
    context.update({'json_grafico_guerra_dia': json.dumps(montar_grafico_7_ultimas_guerras())})
    context.update({'json_grafico_ultimas_siege': json.dumps(montar_grafico_qtd_participacoes_ultimas_siege())})
    context.update({'json_grafico_qtd_classes_guilda': json.dumps(
        montar_grafico_qtd_classes_guilda(all_membros_ativos))})
    context.update({'classes': get_qtd_by_classe(all_membros_ativos)})
    context.update({'quantitativo': get_quantitativos(all_membros_ativos)})
    return render(request, '{0}/index.html'.format(utils.path_estatisticas), context)


def montar_grafico_7_ultimas_guerras():
    hoje = date.today()
    grafico_guerra_dia = []
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
            'dia': '{}/{}'.format(guerra.data_inicio.day, guerra.data_inicio.month),
            'participacoes': participacoes, 'frequencias': frequencias})

    return grafico_guerra_dia


def montar_grafico_qtd_participacoes_ultimas_siege():
    hoje = date.today()
    grafico = []
    ultimas_siege = Guerras.objects.filter(tipo=Guerras.TIPO_SIEGE_ID).exclude(
        data_inicio=hoje).order_by('-data_inicio')[:7]
    ultimas_siege = reversed(ultimas_siege)
    for guerra in ultimas_siege:
        if guerra.tipo == Guerras.TIPO_SIEGE_ID:
            participacoes = ParticiparGuerra.objects.filter(
                guerra=guerra, participa=ParticiparGuerra.PARTICIPAR_SIM)
            participacoes_herois = participacoes.filter(participante__cargo=UserAvancado.CARGO_HEROI_ID).count()
            frequencias = FrequenciaGuerra.objects.filter(guerra=guerra).first()
            if frequencias and frequencias.participantes:
                frequencias_membros = frequencias.participantes.__len__()
            else:
                frequencias_membros = 0
            grafico.append({
                'dia': '{}/{}/{}'.format(guerra.data_inicio.day, guerra.data_inicio.month, guerra.data_inicio.year),
                'participacoes_herois': participacoes_herois, 'frequencias_membros': frequencias_membros})

    return grafico


def montar_grafico_qtd_classes_guilda(all_membros_ativos):
    return get_qtd_by_classe(all_membros_ativos)


def get_qtd_by_classe(all_membros_ativos):
    classes = []
    classes.append({
        'nome': 'Guerreiro', 'cor': '#487d00', 'n': get_numero_classe(all_membros_ativos, 'Guerreiro')
    })
    classes.append({
        'nome': 'Valkyria', 'cor': '#0951ae', 'n': get_numero_classe(all_membros_ativos, 'Valkyria')
    })
    classes.append({
        'nome': 'Berserker', 'cor': '#24c664', 'n': get_numero_classe(all_membros_ativos, 'Berserker')
    })
    classes.append({
        'nome': 'Caçadora', 'cor': '#372fa7', 'n': get_numero_classe(all_membros_ativos, 'Caçadora')
    })
    classes.append({
        'nome': 'Arqueiro', 'cor': '#8b86f5', 'n': get_numero_classe(all_membros_ativos, 'Arqueiro')
    })
    classes.append({
        'nome': 'Mago', 'cor': '#8c387b', 'n': get_numero_classe(all_membros_ativos, 'Mago')
    })
    classes.append({
        'nome': 'Bruxa', 'cor': '#f1d5b6', 'n': get_numero_classe(all_membros_ativos, 'Bruxa')
    })
    classes.append({
        'nome': 'Feiticeira', 'cor': '#571fdf', 'n': get_numero_classe(all_membros_ativos, 'Feiticeira')
    })
    classes.append({
        'nome': 'Ninja', 'cor': '#680d90', 'n': get_numero_classe(all_membros_ativos, 'Ninja')
    })
    classes.append({
        'nome': 'Kunoichi', 'cor': '#7eb2b3', 'n': get_numero_classe(all_membros_ativos, 'Kunoichi')
    })
    classes.append({
        'nome': 'Musa', 'cor': '#174d39', 'n': get_numero_classe(all_membros_ativos, 'Musa')
    })
    classes.append({
        'nome': 'Maehwa', 'cor': '#ee70c7', 'n': get_numero_classe(all_membros_ativos, 'Maehwa')
    })
    classes.append({
        'nome': 'Tamer', 'cor': '#2500fb', 'n': get_numero_classe(all_membros_ativos, 'Tamer')
    })
    classes.append({
        'nome': 'Mística', 'cor': '#9c46ea', 'n': get_numero_classe(all_membros_ativos, 'Mística')
    })
    classes.append({
        'nome': 'Lutador', 'cor': '#aa6173', 'n': get_numero_classe(all_membros_ativos, 'Lutador')
    })
    classes.append({
        'nome': 'Lahn', 'cor': '#6dc08d', 'n': get_numero_classe(all_membros_ativos, 'Lahn')
    })
    classes.append({
        'nome': 'Cavaleira das Trevas', 'cor': '#5c232d', 'n': get_numero_classe(all_membros_ativos, 'Cavaleira das Trevas')
    })
    classes.append({
        'nome': 'Shai', 'cor': '#9ea32b', 'n': get_numero_classe(all_membros_ativos, 'Shai')
    })
    return classes


def get_numero_classe(all_membros_ativos, nome):
    return all_membros_ativos.filter(char_classe__slug=nome).count()


def get_quantitativos(all_membros_ativos):
    import math
    result = {}
    gs_medio = all_membros_ativos.aggregate(Avg('gs')).get('gs__avg')
    pa_medio = all_membros_ativos.aggregate(Avg('char_ap')).get('char_ap__avg')
    paawk_medio = all_membros_ativos.aggregate(Avg('char_ap_despertada')).get('char_ap_despertada__avg')
    pd_medio = all_membros_ativos.aggregate(Avg('char_dp')).get('char_dp__avg')
    result.update({'gs_medio': math.ceil(gs_medio), 'pa_medio': math.ceil(pa_medio),
                   'paawk_medio': math.ceil(paawk_medio), 'pd_medio': math.ceil(pd_medio)})
    return result
