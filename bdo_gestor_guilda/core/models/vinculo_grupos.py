from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.grupos import Grupos


class VinculoGrupos(models.Model):
    id = models.AutoField(primary_key=True)
    membro = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupos, db_column='fk_grupo', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_vinculo_grupos'

    def __str__(self):
        return '{} - Grupo {}'.format(self.membro.nome_familia, self.grupo)
