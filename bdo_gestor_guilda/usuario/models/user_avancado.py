from django.contrib.auth.models import User
from django.db import models

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar


class UserAvancado(models.Model):
    CARGO_NENHUM = 4
    CARGO_MEMBRO = 3
    CARGO_OFICIAL = 2
    CARGO_LIDER = 1
    CARGO_NENHUM_SLUG = 'Não é Membro'
    CARGO_MEMBRO_SLUG = 'Membro'
    CARGO_OFICIAL_SLUG = 'Oficial'
    CARGO_LIDER_SLUG = 'Líder'
    CARGOS = (
        (CARGO_LIDER, "Lider"),

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
    cargo = models.IntegerField(choices=CARGOS, default=CARGO_NENHUM)
    url_print_status = models.CharField(max_length=100)

    ativo = models.BooleanField(default=True)
    justificativa_inativo = models.CharField(max_length=200, null=True, blank=True)

    usuario = models.ForeignKey(User, db_column='fk_user', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_user_avancado'

    def __str__(self):
        return '[{0}] {1}'.format(self.nome_familia, self.nome_char_principal)
