# coding: utf-8
from django import template
from django.utils.html import strip_tags

from bdo_gestor_guilda.core.helpers.masks import Money

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
