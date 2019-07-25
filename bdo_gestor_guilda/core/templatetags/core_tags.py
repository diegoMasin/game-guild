# coding: utf-8
from django import template
from django.utils.html import strip_tags

from bdo_gestor_guilda.core.helpers.masks import Money
from bdo_gestor_guilda.core.models.guerras import Guerras
from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
from bdo_gestor_guilda.core.models.payout import Payout
from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado

register = template.Library()


@register.filter()
def to_mask_money(value):
    return Money().format(value) if value else 'R$ 0,00'


@register.filter()
def format_positivo_negativo(value):
    formato_cor = 'success' if value >= 0 else 'danger'

    return formato_cor


@register.filter()
def format_status_conta(value):
    formato_cor = 'success' if value else 'danger'

    return formato_cor


@register.filter(is_safe=True)
def message_erro_custom(value):
    return strip_tags(value).replace('dict_values', '').replace('([[', '').replace(']])', '').replace('\'', '').replace('.', '. ')


@register.filter()
def format_label_error(value):
    return 'text-danger' if value else ''


@register.filter
def bollean_sim_ou_nao(value):
    return 'Sim' if value or value == 1 else 'Não'


@register.filter
def cor_cargo(value):
    from bdo_gestor_guilda.usuario.models import UserAvancado
    cor = 'success'
    if value == UserAvancado.CARGO_LIDER_SLUG:
        cor = 'danger'
    if value == UserAvancado.CARGO_OFICIAL_SLUG:
        cor = 'warning'
    return cor


@register.simple_tag
def get_frequencia_tipo_guerra_by_payout(usuario, guerras_by_payout):
    return FrequenciaGuerra.objects.filter(guerra__pk__in=guerras_by_payout.values_list('pk', flat=True),
                                           participantes__contains=[usuario.pk]).count()
