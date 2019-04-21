from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bdo_gestor_guilda.core.helpers import utils
from bdo_gestor_guilda.usuario.forms.user import UserModelForm
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.usuario.forms.user_avancado import UserAvancadoForm


def signup(request):
    form = UserModelForm(request.POST or None)

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
            userqueryset = User.objects.all().filter(email=request.POST['username'])
            if userqueryset:
                username = userqueryset[0].username
                user = authenticate(request, username=username, password=request.POST['password'])

        if user is not None:
            login(request, user)
            dados_user_avancado = UserAvancado.objects.filter(usuario=user)

            if dados_user_avancado.first() and not dados_user_avancado.first().ativo:
                return redirect(utils.url_name_aguarde_aprovacao)

            if not dados_user_avancado:
                return redirect(utils.url_name_cadastrar_user_avancado)

            messages.success(request, 'Bem Vindo à OXION GUILD!')
            return redirect(utils.url_name_home)
        else:
            messages.warning(request, 'Usuário ou senha não existente!')

    form.fields['username'].initial = request.session.get(user_remember_cookie, '')
    utils.context['form'] = form
    utils.context[user_remember_cookie] = request.session.get(user_remember_cookie, False)
    return render(request, '{0}/login.html'.format(utils.path_template_login), utils.context)


@login_required
def do_logout(request):
    user_remember = request.session.get('userremember', False)
    logout(request)

    if user_remember is not False:
        request.session['userremember'] = user_remember

    messages.success(request, 'Saiu com Sucesso!')
    return redirect(utils.url_name_login)


def termo(request):
    return render(request, '{0}/termo_de_uso.html'.format(utils.path_template_login), utils.context)


@login_required
def cadastrar_user_avancado(request):
    form = UserAvancadoForm()
    context = utils.get_context(request)
    context.update({'form': form})
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
    return render(request, '{0}/aguarde_aprovacao.html'.format(utils.path_user_avancado), utils.context)
