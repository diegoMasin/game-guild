from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.forms.guerras import GuerrasForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.configuracoes import Configuracoes


@login_required
def index(request):
    context = utils.get_context(request)
    if context.get('dados_avancados').is_lider():
        todas_configuracoes = Configuracoes.objects.all().order_by('pk')
        context.update({'todas_configuracoes': todas_configuracoes})
        return render(request, '{0}/index.html'.format(utils.path_configuracoes), context)
    return redirect(utils.url_name_home)


@login_required
def atualizar(request, conf_id):
    try:
        if request.method == 'POST':
            conf = Configuracoes.objects.get(pk=conf_id)
            esta_valido, mensagem = validacao_geral(conf)
            if esta_valido:
                valor = request.POST.get('valor_conf')
                if conf.tipo_variavel == conf.STRING_ID:
                    conf.valor_string = valor
                elif conf.tipo_variavel == conf.INTEIRO_ID:
                    conf.valor_inteiro = valor
                elif conf.tipo_variavel == conf.BOOL_ID:
                    conf.valor_bool = valor
                conf.save()
                messages.success(request, 'A variável ({}) foi atualizada com Sucesso!'.format(conf.slug_variavel))
            else:
                messages.warning(request, mensagem)
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
    return HttpResponseRedirect(reverse(utils.url_configuracoes_index))


def validacao_geral(conf):
    validado = True
    mensagem = ''
    return validado, mensagem


def contador_de_registros(request):
    return 0
