import re
from django.contrib.auth.models import User
from django.db import models

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar


class UserAvancado(models.Model):
    CARGO_HEROI_ID = 6
    CARGO_QUARTEL_MESTRE_ID = 5
    CARGO_NENHUM_ID = 4
    CARGO_MEMBRO_ID = 3
    CARGO_OFICIAL_ID = 2
    CARGO_LIDER_ID = 1
    CARGO_HEROI_SLUG = 'Herói'
    CARGO_QUARTEL_MESTRE_SLUG = 'Quartel-mestre'
    CARGO_NENHUM_SLUG = 'Não é Membro'
    CARGO_MEMBRO_SLUG = 'Membro'
    CARGO_OFICIAL_SLUG = 'Oficial'
    CARGO_LIDER_SLUG = 'Líder'
    CARGOS = (
        (CARGO_LIDER_ID, CARGO_LIDER_SLUG),
        (CARGO_OFICIAL_ID, CARGO_OFICIAL_SLUG),
        (CARGO_QUARTEL_MESTRE_ID, CARGO_QUARTEL_MESTRE_SLUG),
        (CARGO_MEMBRO_ID, CARGO_MEMBRO_SLUG),
        (CARGO_HEROI_ID, CARGO_HEROI_SLUG)
    )
    RECRUTA = (
        (CARGO_MEMBRO_ID, CARGO_MEMBRO_SLUG),
        (CARGO_HEROI_ID, CARGO_HEROI_SLUG)
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
    url_bdo_planner = models.CharField(max_length=100, null=True, blank=True)
    siege = models.BooleanField(choices=SIM_OU_NAO, default=True)
    node_seg = models.BooleanField(default=False)
    node_ter = models.BooleanField(default=False)
    node_qua = models.BooleanField(default=False)
    node_qui = models.BooleanField(default=False)
    node_sex = models.BooleanField(default=False)
    node_dom = models.BooleanField(default=False)

    cargo = models.IntegerField(choices=CARGOS, default=CARGO_NENHUM_ID)
    ativo = models.BooleanField(default=False)
    recruta_para_ser = models.IntegerField(choices=RECRUTA, default=CARGO_MEMBRO_ID)
    justificativa_inativo = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.ForeignKey(User, db_column='fk_user', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_user_avancado'

    def __str__(self):
        return '{0} ({1})'.format(self.nome_familia, self.nome_char_principal)

    def is_lider(self):
        return self.cargo == self.CARGO_LIDER_ID

    def is_oficial(self):
        return self.cargo == self.CARGO_OFICIAL_ID

    def is_membro(self):
        return self.cargo == self.CARGO_MEMBRO_ID

    def is_lider_or_oficial(self):
        return self.cargo == self.CARGO_OFICIAL_ID or self.cargo == self.CARGO_LIDER_ID

    def is_heroi(self):
        return self.cargo == self.CARGO_HEROI_ID

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
        if self.cargo == self.CARGO_HEROI_ID:
            cargo = self.CARGO_HEROI_SLUG
        return cargo

    def get_slug_candidato(self):
        candidato = ''
        if self.recruta_para_ser == self.CARGO_MEMBRO_ID:
            candidato = self.CARGO_MEMBRO_SLUG
        if self.recruta_para_ser == self.CARGO_HEROI_ID:
            candidato = self.CARGO_HEROI_SLUG
        return candidato

    def get_pt_fixa(self):
        from bdo_gestor_guilda.core.models.grupos import Grupos
        from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos
        pt_fixa = ''
        lider_user_logado = Grupos.objects.filter(lider=self).first()
        membro_user_logado = VinculoGrupos.objects.filter(membro=self).first()
        if lider_user_logado:
            pt_fixa = 'Líder do(a) {}'.format(lider_user_logado)
        if membro_user_logado:
            pt_fixa = 'Membro do(a) {}'.format(membro_user_logado.grupo)
        return pt_fixa

    def get_color_participa_guerra_hoje(self):
        from datetime import date
        from bdo_gestor_guilda.core.models.guerras import Guerras
        from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
        guerra_de_hoje = Guerras.objects.filter(data_inicio=date.today()).first()
        is_participa_guerra_hoje = ParticiparGuerra.objects.filter(guerra=guerra_de_hoje, participante=self).first()
        result = ''
        if is_participa_guerra_hoje:
            result = is_participa_guerra_hoje.get_color_participa()
        return result

    def get_logo_pequena(self):
        return 'v1/global/assets/images/logo_classes/{0}.png'.format(self.char_classe.nome_classe)

    def muita_ausencia_ultimas_guerras(self):
        from datetime import date
        from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
        from bdo_gestor_guilda.core.models.guerras import Guerras
        from bdo_gestor_guilda.core.helpers import utils
        hoje = date.today()
        constante_de_aceitacao_para_frequencia = utils.get_variavel_frequencia_alerta()
        ultimas_7_guerras = Guerras.objects.all().exclude(data_inicio=hoje).order_by('-data_inicio')[:7]
        frequencia = FrequenciaGuerra.objects.filter(
            guerra__in=ultimas_7_guerras, participantes__contains=[self.pk]).count()
        return True if frequencia <= constante_de_aceitacao_para_frequencia else False

    def get_todas_guerras_disponiveis(self):
        from bdo_gestor_guilda.core.models.guerras import Guerras
        data_entrou_sistema = self.usuario.date_joined
        return Guerras.objects.filter(data_inicio__gte=data_entrou_sistema, tipo=Guerras.TIPO_NODEWAR_ID)

    def get_total_guerras(self):
        return self.get_todas_guerras_disponiveis().count()

    def get_total_participacoes_guerras(self):
        from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
        todas_guerras = self.get_todas_guerras_disponiveis()
        return ParticiparGuerra.objects.filter(guerra__in=todas_guerras, participante=self).count()

    def get_total_frequencias_guerras(self):
        from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
        todas_guerras = self.get_todas_guerras_disponiveis()
        return FrequenciaGuerra.objects.filter(
            guerra__in=todas_guerras, participantes__contains=[self.pk]).count()

    def get_todas_siege_disponiveis(self):
        from bdo_gestor_guilda.core.models.guerras import Guerras
        data_entrou_sistema = self.usuario.date_joined
        return Guerras.objects.filter(data_inicio__gte=data_entrou_sistema, tipo=Guerras.TIPO_SIEGE_ID)

    def get_total_sieges(self):
        return self.get_todas_siege_disponiveis().count()

    def get_total_participacoes_guerras(self):
        from bdo_gestor_guilda.core.models.participar_guerra import ParticiparGuerra
        todas_guerras = self.get_todas_siege_disponiveis()
        return ParticiparGuerra.objects.filter(guerra__in=todas_guerras, participante=self).count()

    def get_total_frequencias_guerras(self):
        from bdo_gestor_guilda.core.models.frequencia_guerra import FrequenciaGuerra
        todas_guerras = self.get_todas_siege_disponiveis()
        return FrequenciaGuerra.objects.filter(
            guerra__in=todas_guerras, participantes__contains=[self.pk]).count()
