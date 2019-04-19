from django.contrib import messages
from django.contrib.messages import constants
from django.utils.translation import ugettext_lazy as _


def form_errors_format(request, fail_silently=False, form=None, typifying=constants.WARNING, exception=None,
                       with_title=None):
    """
    Adds a message with the ``WARNING`` level.
    :param with_title:
    :param exception:
    :param typifying:
    :param form:
    :param request:
    :param fail_silently:
    """

    message = ''
    if form:
        message = _create_form_text_html(form, with_title)

    if str(exception):
        messages.add_message(request, typifying, exception, extra_tags='', fail_silently=fail_silently)

    if 'message' in locals() and message is not None:
        messages.add_message(request, typifying, message, extra_tags='', fail_silently=fail_silently)


def _create_form_text_html(form, with_title):
    html_messages = ''
    for field in form.fields:
        if len(form[field].errors) > 0:
            html_messages += '<li>{0}'.format(form[field].label)
            html_messages += '<ul>'
            for message in form[field].errors:
                html_messages += '<li>&bull; {0}</li>'.format(message)
            html_messages += '</ul>'
            html_messages += '</li>'

    for error in form.errors:
        if error not in form.fields:
            html_messages += '<li>{0}'.format('Atenção!' if error == '__all__' else error)
            html_messages += '<ul>'
            for message in form.errors[error]:
                html_messages += '<li>&bull; {0}</li>'.format(message)
            html_messages += '</ul>'
            html_messages += '</li>'

    if not html_messages:
        return None

    html_title = ''
    if with_title:
        html_title = '<h5>Verifique o(s) seguinte(s) erro(s):</h5>'

    return '{0}<ul class="list-unstyled">{1}</ul>'.format(html_title, html_messages)


class TextosPadroes(object):
    @staticmethod
    def salvar():
        return _('Registro gravado com sucesso.')

    @staticmethod
    def deletar():
        return _('Registro deletado com sucesso.')

    @staticmethod
    def deletar_erro():
        return _('Não foi possível remover o registro.')

    @staticmethod
    def error(erro):
        return _('Erro encontrado, contate o administrador do sistema.\n\n {0}'.format(erro))

    @staticmethod
    def error_deletion():
        return _('O registro não pode ser excluído, entre em contato com o Setor de TI.')

    @staticmethod
    def select_option():
        return _('Todos')

    @staticmethod
    def fomulario_invalido():
        return _('Formulário não está válido. {}')

    @staticmethod
    def sem_registros():
        return _('Sem registros.')

    @staticmethod
    def empty():
        return _('Selecione...')

    @staticmethod
    def filtro_sem_registros():
        return _('Não há registros respectivos ao(s) filtro(s) selecionado(s).')

    @staticmethod
    def data_inicio_maior_que_data_fim():
        return _('A data de início não pode ser maior que a data de término.')

    @staticmethod
    def campo_obrigatorio():
        return _('Este campo é obrigatório.')

    @staticmethod
    def existem_registros_conflitantes():
        return _('Existem registros conflitantes.')

    @staticmethod
    def usuario_nao_logado():
        return _('Usuário não esta logado, por favor efetuar o login!')

    @staticmethod
    def error_padrao():
        return _('Ocorreu um erro. Tente novamente mais tarde.')

    @staticmethod
    def apagar_sucesso_o(modelo):
        return _('{0} removido com sucesso.'.format(modelo))

    @staticmethod
    def apagar_sucesso_a(modelo):
        return _('{0} removida com sucesso.'.format(modelo))

    @staticmethod
    def atualizar_sucesso_o(modelo):
        return _('{0} atualizado com sucesso.'.format(modelo))

    @staticmethod
    def atualizar_sucesso_a(modelo):
        return _('{0} atualizada com sucesso.'.format(modelo))

    @staticmethod
    def salvar_sucesso_o(modelo):
        return _('Novo {0} criado com sucesso.'.format(modelo))

    @staticmethod
    def salvar_sucesso_a(modelo):
        return _('Nova {0} criada com sucesso.'.format(modelo))
