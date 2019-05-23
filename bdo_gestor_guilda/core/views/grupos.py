from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.forms.grupos import GruposForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos


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
                grupos_atuais = Grupos.objects.filter(lider=dados.get('lider'))
                if grupos_atuais.count() == 0:
                    Grupos(**dados).save()
                    messages.success(request, TextosPadroes.salvar_sucesso_o('Grupo'))
                else:
                    messages.error(request, '{} já é lider em outro grupo fixo.'.format(dados.get('lider')))
                    return redirect(utils.url_grupos_cadastrar)
            else:
                erros_form = utils.TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
                return redirect(utils.url_grupos_cadastrar)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
        return redirect(utils.url_grupos_cadastrar)
    return redirect(utils.url_grupos_listar)

@login_required
def deletar(request, grupo_id):
    try:
        context = utils.get_context(request)
        grupo = Grupos.objects.filter(pk=grupo_id).first()
        membros = VinculoGrupos.objects.filter(grupo=grupo)
        if grupo:
            if membros:
                membros.delete()
            grupo.delete()
            messages.success(request, '{0} Deletado com Sucesso!'.format(grupo))
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
