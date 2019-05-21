from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class Grupos(models.Model):
    id = models.AutoField(primary_key=True)
    lider = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_grupos'

    def __str__(self):
        return '{}'.format(self.titulo)
