from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.forms.grupos import GruposForm
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes


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


@login_required
def inserir(request):
    try:
        if request.method == 'POST':
            form = GruposForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                user_avancado = UserAvancado.objects.filter(usuario=request.user).first()
                grupos_atuais = Grupos.objects.filter(lider=user_avancado)
                if grupos_atuais.count() == 0:
                    Grupos(**dados).save()
                    messages.success(request, TextosPadroes.salvar_sucesso_o('Grupo'))
                else:
                    messages.error(request, '{} já é lider em outro grupo fixo.'.format(dados.get('lider')))
            else:
                erros_form = utils.TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
                return redirect(utils.url_grupos_cadastrar)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
        return redirect(utils.url_grupos_cadastrar)
    return redirect(utils.url_grupos_listar)
