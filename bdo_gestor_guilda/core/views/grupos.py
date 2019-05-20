from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.forms.grupos import GruposForm


@login_required
def listar(request):
    context = utils.get_context(request)
    grupos = Grupos.objects.all().order_by('data_cadastro')
    context.update({'grupos': grupos})
    return render(request, '{0}/index.html'.format(utils.path_grupos), context)


@login_required
def cadastrar(request):
    context = utils.get_context(request)
    context.update({'form': GruposForm()})
    return render(request, '{0}/cadastrar.html'.format(utils.path_grupos), context)
