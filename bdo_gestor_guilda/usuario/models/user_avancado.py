from django.contrib.auth.models import User
from django.db import models

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar


class UserAvancado(models.Model):
    CARGO_NENHUM_ID = 4
    CARGO_MEMBRO_ID = 3
    CARGO_OFICIAL_ID = 2
    CARGO_LIDER_ID = 1
    CARGO_NENHUM_SLUG = 'Não é Membro'
    CARGO_MEMBRO_SLUG = 'Membro'
    CARGO_OFICIAL_SLUG = 'Oficial'
    CARGO_LIDER_SLUG = 'Líder'
    CARGOS = (
        (CARGO_LIDER_ID, CARGO_LIDER_SLUG),
        (CARGO_OFICIAL_ID, CARGO_OFICIAL_SLUG),
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
