from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.forms.grupos import GruposForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos


@login_required
def listar(request):
    context = utils.get_context(request)
    grupos = Grupos.objects.all().order_by('titulo')
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
                is_lider_grupo = Grupos.objects.filter(lider=dados.get('lider')).count() > 0
                is_membro_grupo = VinculoGrupos.objects.filter(membro=dados.get('lider')).count() > 0
                if not is_lider_grupo and not is_membro_grupo:
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


@login_required
def editar(request, grupo_id):
    try:
        grupo = Grupos.objects.get(pk=grupo_id)
        context = utils.get_context(request)
        context.update({'form': GruposForm(instance=grupo)})
        context.update({'grupo': grupo})
        membros = VinculoGrupos.objects.filter(grupo=grupo)
        context.update({'membros': membros})
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_grupos_listar))
    return render(request, '{0}/editar.html'.format(utils.path_grupos), context)


@login_required
def atualizar(request, grupo_id):
    try:
        if request.method == 'POST':
            grupo = Grupos.objects.get(pk=grupo_id)
            form = GruposForm(request.POST, instance=grupo)
            if form.has_changed():
                if form.is_valid():
                    dados = form.cleaned_data
                    dados['id'] = grupo_id
                    Grupos(**dados).save()
                    messages.success(request, utils.TextosPadroes.atualizar_sucesso_o(grupo))
                else:
                    erros_form = utils.TextosPadroes.errors_form(form)
                    for error in erros_form:
                        messages.warning(request, error)
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_grupos_editar, args=[grupo_id]))
    return HttpResponseRedirect(reverse(utils.url_grupos_editar, args=[grupo_id]))
