import re

from django.contrib.auth.models import User
from django.db import models

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar


class UserAvancado(models.Model):
    CARGO_QUARTEL_MESTRE_ID = 5
    CARGO_NENHUM_ID = 4
    CARGO_MEMBRO_ID = 3
    CARGO_OFICIAL_ID = 2
    CARGO_LIDER_ID = 1
    CARGO_QUARTEL_MESTRE_SLUG = 'Quartel-mestre'
    CARGO_NENHUM_SLUG = 'Não é Membro'
    CARGO_MEMBRO_SLUG = 'Membro'
    CARGO_OFICIAL_SLUG = 'Oficial'
    CARGO_LIDER_SLUG = 'Líder'
    CARGOS = (
        (CARGO_LIDER_ID, CARGO_LIDER_SLUG),
        (CARGO_OFICIAL_ID, CARGO_OFICIAL_SLUG),
        (CARGO_QUARTEL_MESTRE_ID, CARGO_QUARTEL_MESTRE_SLUG),
        (CARGO_MEMBRO_ID, CARGO_MEMBRO_SLUG)
    )
    SIM_OU_NAO = (
        (True, 'Sim'),
        (False, 'Não')
    )

    id = models.AutoField(primary_key=True)
    user_discord = models.CharField(max_length=50)
    nome_familia = models.CharField(max_length=30)
    nome_char_principal = models.CharField(max_length=30)
    char_lvl = models.IntegerField()
    char_classe = models.ForeignKey(TipoClasseChar, db_column='fk_tipo_classe_char', on_delete=models.PROTECT)
    char_ap = models.IntegerField()
    char_ap_despertada = models.IntegerField()
    char_dp = models.IntegerField()
    gs = models.IntegerField()
    url_print_status = models.CharField(max_length=100)
    siege = models.BooleanField(choices=SIM_OU_NAO, default=True)
    node_seg = models.BooleanField(default=False)
    node_ter = models.BooleanField(default=False)
    node_qua = models.BooleanField(default=False)
    node_qui = models.BooleanField(default=False)
    node_sex = models.BooleanField(default=False)
    node_dom = models.BooleanField(default=False)

    cargo = models.IntegerField(choices=CARGOS, default=CARGO_NENHUM_ID)
    ativo = models.BooleanField(default=False)
    justificativa_inativo = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.ForeignKey(User, db_column='fk_user', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_user_avancado'

    def __str__(self):
        return '[{0}] {1}'.format(self.nome_familia, self.nome_char_principal)

    def is_lider(self):
        return True if self.cargo == self.CARGO_LIDER_ID else False

    def is_oficial(self):
        return True if self.cargo == self.CARGO_OFICIAL_ID else False

    def is_lider_or_oficial(self):
        return True if self.cargo == self.CARGO_OFICIAL_ID or self.cargo == self.CARGO_LIDER_ID else False

    def get_dias_nodewar(self):
        dias = []
        if self.node_seg:
            dias.append('Segunda')
        if self.node_ter:
            dias.append('Terça')
        if self.node_qua:
            dias.append('Quarta')
        if self.node_qui:
            dias.append('Quinta')
        if self.node_sex:
            dias.append('Sexta')
        if self.node_dom:
            dias.append('Domingo')
        return dias

    def get_dias_nodewar_format(self):
        dias = self.get_dias_nodewar()
        format = ''
        for dia in dias:
            format = '{}{}, '.format(format, dia)
        return format[0:-2]

    def joga_nodewar(self):
        joga = False
        if self.node_seg or self.node_ter or self.node_qua or self.node_qui or self.node_sex or self.node_dom:
            joga = True
        return joga

    def get_url_print(self):
        url = self.url_print_status
        if not ('http://' in url or 'https://' in url):
            url = 'http://{0}'.format(url)
        return url

    def pode_ser_promovido(self):
        pode = False
        if self.cargo == self.CARGO_MEMBRO_ID:
            pode = True
        elif self.cargo == self.CARGO_OFICIAL_ID:
            pode = True if UserAvancado.objects.filter(cargo=self.CARGO_LIDER_ID).count() < 2 else False
        return pode

    def pode_ser_rebaixado(self):
        return True if self.cargo == self.CARGO_OFICIAL_ID or self.cargo == self.CARGO_LIDER_ID else False

    def get_slug_cargo(self):
        cargo = ''
        if self.cargo == self.CARGO_LIDER_ID:
            cargo = self.CARGO_LIDER_SLUG
        if self.cargo == self.CARGO_MEMBRO_ID:
            cargo = self.CARGO_MEMBRO_SLUG
        if self.cargo == self.CARGO_OFICIAL_ID:
            cargo = self.CARGO_OFICIAL_SLUG
        return cargo

    def get_grupos_fixo_lider(self):
        from bdo_gestor_guilda.core.models.grupos import Grupos
        lider_grupos = Grupos.objects.filter(lider=self)
        format = ''
        for grupo in lider_grupos:
            format = '{}{}, '.format(format, grupo)
        return format[0:-2]
