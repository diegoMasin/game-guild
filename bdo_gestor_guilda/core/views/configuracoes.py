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
    todas_configuracoes = Configuracoes.objects.all()
    context.update({'todas_configuracoes': todas_configuracoes})
    return render(request, '{0}/index.html'.format(utils.path_configuracoes), context)
