from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from django.contrib.auth.models import User
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.forms.guerras import GuerrasForm


@login_required
def listar(request):
    context = utils.get_context(request)
    if context.get('is_lider_or_oficial'):
        todas_guerras = Guerras.objects.all().order_by('-pk')
        context.update({'todas_guerras': todas_guerras})
        return render(request, '{0}/index.html'.format(utils.path_guerras), context)
    return redirect(utils.url_name_home)


@login_required
def cadastrar(request):
    form = GuerrasForm()
    context = utils.get_context(request)
    context.update({'form': form})
    return render(request, '{0}/cadastrar.html'.format(utils.path_guerras), utils.context)


@login_required
def inserir(request):
    try:
        if request.method == 'POST':
            form = GuerrasForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                Guerras(**dados).save()
                messages.success(request, TextosPadroes.salvar_sucesso_a('Guerra'))
                return redirect(utils.url_guerras_listar)
            else:
                erros_form = TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
    return redirect(utils.url_guerras_cadastrar)
