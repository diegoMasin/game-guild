from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.forms.anuncios_gerais import AnunciosGeraisForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.anuncios_gerais import AnunciosGerais
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


@login_required
def cadastrar(request):
    context = utils.get_context(request)
    context.update({'form': AnunciosGeraisForm()})
    return render(request, '{0}/cadastrar.html'.format(utils.path_anuncios_gerais), context)


@login_required
def inserir(request):
    try:
        if request.method == 'POST':
            form = AnunciosGeraisForm(request.POST)
            if form.is_valid():
                usuario = UserAvancado.objects.filter(usuario=request.user).first()
                dados = form.cleaned_data
                dados['usuario'] = usuario
                AnunciosGerais(**dados).save()
                messages.success(request, TextosPadroes.salvar_sucesso_o('Anúncio'))
            else:
                erros_form = utils.TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
                return redirect(utils.url_anuncios_gerais_cadastrar)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
        return redirect(utils.url_anuncios_gerais_cadastrar)
    return redirect(utils.url_name_home)
#
#
# @login_required
# def deletar(request, vinculo_grupo_id):
#     try:
#         context = utils.get_context(request)
#         membro = VinculoGrupos.objects.get(pk=vinculo_grupo_id)
#         membro.delete()
#         messages.success(request, '{0} Removido com Sucesso!'.format(membro))
#     except Exception as e:
#         messages.error(request, utils.TextosPadroes.erro_padrao())
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
