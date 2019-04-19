from django.contrib.auth.models import User
from django.db import models

from bdo_gestor_guilda.usuario.models.tipo_classe_char import TipoClasseChar


class UserAvancado(models.Model):
    id = models.AutoField(primary_key=True)
    nome_real = models.CharField(max_length=50)
    nome_familia = models.CharField(max_length=30)
    nome_char_principal = models.CharField(max_length=30)
    char_lvl = models.IntegerField()
    char_classe = models.ForeignKey(TipoClasseChar, db_column='fk_tipo_classe_char', on_delete=models.PROTECT)

    usuario = models.ForeignKey(User, db_column='fk_user', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_user_avancado'

    def __str__(self):
        return '[{0}] {1}'.format(self.nome_familia, self.nome_char_principal)
