from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class AnunciosGerais(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=800)
    usuario = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_anuncios_gerais'
