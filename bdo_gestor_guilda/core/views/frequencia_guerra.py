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
    guerra = Guerras.objects.filter(pk=int(guerra_id)).first()
    participacoes_guerra = ParticiparGuerra.objects.filter(
        guerra__pk=int(guerra_id)).order_by('participante__nome_familia')
    url_marcar = reverse(utils.url_frequencia_guerra_marcar)
    context.update({'guerra': guerra})
    context.update({'participacoes_guerra': participacoes_guerra})
    context.update({'url_marcar': url_marcar})
    return render(request, '{0}/marcar_frequencia.html'.format(utils.path_guerras), context)


@login_required
def marcar(request):
    import json
    from django.http import HttpResponse
    data = {'sucesso': True}
    try:
        if request.method == 'GET':
            lista_frequencia = []
            guerra_id = int(request.GET.get('guerra'))
            user_avancado_id = int(request.GET.get('user_avancado'))
            tem_frequencia = FrequenciaGuerra.objects.filter(guerra=guerra_id)
            if tem_frequencia:
                frequencia_guerra = tem_frequencia.first()
                ja_frequente = tem_frequencia.filter(participantes__contains=[user_avancado_id]).count() > 0
                if ja_frequente:
                    lista_frequencia = frequencia_guerra.participantes
                    lista_frequencia.remove(user_avancado_id)
                    frequencia_guerra.participantes = lista_frequencia
                    frequencia_guerra.save()
                else:
                    lista_frequencia = frequencia_guerra.participantes
                    lista_frequencia.append(user_avancado_id)
                    frequencia_guerra.participantes = lista_frequencia
                    frequencia_guerra.save()
            else:
                lista_frequencia.append(user_avancado_id)
                guerra = Guerras.objects.filter(pk=guerra_id).first()
                dados = {'guerra': guerra, 'participantes': lista_frequencia}
                FrequenciaGuerra(**dados).save()
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
