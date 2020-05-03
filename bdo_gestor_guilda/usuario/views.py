from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.core.models.termo_condicoes import TermoCondicoes
from bdo_gestor_guilda.usuario.forms.user import UserModelForm
from bdo_gestor_guilda.usuario.forms.user_avancado import UserAvancadoEditarForm
from bdo_gestor_guilda.usuario.forms.user_avancado import UserAvancadoForm
from bdo_gestor_guilda.usuario.models.recruta_reprovado import RecrutaReprovado
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from django.conf import settings


def signup(request):
    form = UserModelForm(request.POST or None)
    termo = TermoCondicoes.objects.all().last()
    utils.context['termo_texto'] = termo.texto

    if request.method == 'POST':
        if form.is_valid():
            try:
                email_form = form.cleaned_data.get('email')
                existe_email = User.objects.filter(email=email_form).count()
                if existe_email > 0:
                    raise Exception('Esse email já foi cadastrado. Utilize outro.')

                is_check_termo = request.POST.get('check_termo', False)
                if not is_check_termo:
                    raise Exception('Marque caixa se concorda com os Termos e Condições!')

                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')

                return redirect('/login')

            except Exception as e:
                messages.warning(request, e)
        else:
            if form.errors['username']:
                messages.warning(request, form.errors['username'][0])

    utils.context['form'] = form
    return render(request, '{0}/signup.html'.format(utils.path_template_login), utils.context)


def do_login(request):
    form = UserModelForm(request.POST or None)
    user_remember_cookie = 'userremember'
    user_inativo = False

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        is_check_remember = request.POST.get('check_remember', False)

        if is_check_remember:
            if request.session.get(user_remember_cookie, False) is False or request.session[user_remember_cookie] != request.POST['username']:
                request.session[user_remember_cookie] = request.POST['username']
        else:
            if request.session.get(user_remember_cookie, False) is not False:
                del request.session[user_remember_cookie]

        if user is None:
            verifica_user = User.objects.all()
            logouse_com_usuario = verifica_user.filter(username=request.POST['username'])
            logouse_com_email = verifica_user.filter(email=request.POST['username'])
            if logouse_com_email:
                username = logouse_com_email.first().username
                user = authenticate(request, username=username, password=request.POST['password'])

            if logouse_com_usuario:
                if not logouse_com_usuario.first().is_active:
                    user_inativo = True
            if logouse_com_email:
                if not logouse_com_email.first().is_active:
                    user_inativo = True

        if user is not None:
            login(request, user)
            dados_user_avancado = UserAvancado.objects.filter(usuario=user)

            if dados_user_avancado.first() and not dados_user_avancado.first().ativo:
                return redirect(utils.url_name_aguarde_aprovacao)

            if not dados_user_avancado:
                return redirect(utils.url_name_cadastrar_user_avancado)

            messages.success(request, 'Bem Vindo ao sistema Game Guild!')
            return redirect(utils.url_name_home)
        else:
            if user_inativo:
                messages.error(request,
                               'VOCÊ ERA MEMBRO, MAS FOI DESATIVADO! Procure um Oficial ou Líder se deseja voltar.')
            else:
                messages.warning(request, 'Usuário ou senha não existente!')

    form.fields['username'].initial = request.session.get(user_remember_cookie, '')
    form.fields['username'].widget.attrs['placeholder'] = 'Usuário ou Email'
    utils.context['form'] = form
    utils.context[user_remember_cookie] = request.session.get(user_remember_cookie, False)
    utils.context['nome_logo'] = settings.NOME_LOGO
    utils.context['nome_logo_login'] = settings.NOME_LOGO_LOGIN
    utils.context['nome_logo_icon'] = settings.NOME_LOGO_ICON
    return render(request, '{0}/login.html'.format(utils.path_template_login), utils.context)


@login_required
def do_logout(request):
    user_remember = request.session.get('userremember', False)
    logout(request)

    if user_remember is not False:
        request.session['userremember'] = user_remember

    messages.success(request, 'Saiu com Sucesso!')
    return redirect(utils.url_name_login)


@login_required
def cadastrar_user_avancado(request):
    form = UserAvancadoForm()
    context = utils.get_context(request)
    context.update({'form': form})
    justificativa_de_reprovacao = RecrutaReprovado.objects.filter(usuario=request.user).last()
    context.update({'justificativa': justificativa_de_reprovacao})
    return render(request, '{0}/cadastrar.html'.format(utils.path_user_avancado), utils.context)


@login_required
def inserir_user_avancado(request):
    try:
        if request.method == 'POST':
            form = UserAvancadoForm(request.POST)
            if form.is_valid():
                dados = form.cleaned_data
                if UserAvancado.objects.all().count() == 0:
                    dados['ativo'] = True
                    dados['cargo'] = UserAvancado.CARGO_LIDER_ID
                data = utils.set_usuario_owner(request, dados)
                UserAvancado(**data).save()
                messages.success(request, 'Cadastro das Informações feito com Sucesso!')
                return redirect(utils.url_name_aguarde_aprovacao)
            else:
                messages.warning(request, 'Ocorreu algum erro nos campos do Cadastro! Tente Novamente mais tarde.')
                return redirect(utils.url_name_cadastrar_user_avancado)
    except Exception as e:
        messages.warning(request, 'Ocorreu algum erro inesperado! Tente Novamente mais tarde.')
        return redirect(utils.url_name_cadastrar_user_avancado)
    return redirect(utils.url_name_logout)


@login_required
def aguarde_aprovacao(request):
    context = utils.get_context(request)
    return render(request, '{0}/aguarde_aprovacao.html'.format(utils.path_user_avancado), context)


@login_required
def editar_perfil(request):
    try:
        context = utils.get_context(request)
        context.update({'form': UserAvancadoEditarForm(instance=context.get('dados_avancados'))})
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_name_home))
    return render(request, '{0}/editar.html'.format(utils.path_user_avancado), context)


@login_required
def atualizar_perfil(request, user_avancado_id):
    try:
        if request.method == 'POST':
            user_avancado = UserAvancado.objects.get(pk=user_avancado_id)
            form = UserAvancadoEditarForm(request.POST, instance=user_avancado)
            if form.has_changed():
                if form.is_valid():
                    dados = form.cleaned_data
                    dados['id'] = user_avancado_id
                    data = utils.set_usuario_owner(request, dados)
                    UserAvancado(**data).save()
                    messages.success(request, utils.TextosPadroes.atualizar_sucesso_o(user_avancado))
                else:
                    erros_form = utils.TextosPadroes.errors_form(form)
                    for error in erros_form:
                        messages.warning(request, error)
    except Exception as e:
        messages.error(request, utils.TextosPadroes.erro_padrao())
        return HttpResponseRedirect(reverse(utils.url_name_home))
    return HttpResponseRedirect(reverse(utils.url_usuario_editar_perfil))


def reset_senha(request):
    from bdo_gestor_guilda.usuario.forms.reset_senha import ResetSenhaForm
    utils.context['form'] = ResetSenhaForm()
    return render(request, '{0}/index.html'.format(utils.path_recover), utils.context)
