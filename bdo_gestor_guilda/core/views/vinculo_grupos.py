from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.forms.vinculo_grupos import VinculoGruposForm
from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.helpers.default_texts import TextosPadroes
from bdo_gestor_guilda.core.models.grupos import Grupos
from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos


@login_required
def cadastrar(request):
    context = utils.get_context(request)
    context.update({'form': VinculoGruposForm()})
    return render(request, '{0}/cadastrar.html'.format(utils.path_vinculo_grupos), context)


@login_required
def inserir(request):
    try:
        if request.method == 'POST':
            form = VinculoGruposForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                membro = dados.get('membro')
                is_lider_grupo = Grupos.objects.filter(lider=membro).count() > 0
                is_membro_grupo = VinculoGrupos.objects.filter(membro=membro).count() > 0
                if not is_lider_grupo and not is_membro_grupo:
                    VinculoGrupos(**dados).save()
                    messages.success(request, TextosPadroes.salvar_sucesso_o('Vinculo'))
                else:
                    messages.error(request, '{} já é líder ou membro em outro grupo fixo.'.format(membro))
                    return redirect(utils.url_vinculo_grupos_cadastrar)
            else:
                erros_form = utils.TextosPadroes.errors_form(form)
                for error in erros_form:
                    messages.warning(request, error)
                return redirect(utils.url_vinculo_grupos_cadastrar)
    except Exception as e:
        messages.warning(request, TextosPadroes.erro_padrao())
        return redirect(utils.url_vinculo_grupos_cadastrar)
    return redirect(utils.url_grupos_listar)
