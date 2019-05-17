from django.contrib.auth.models import User
from django.db import models


class RecrutaReprovado(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, db_column='fk_user', on_delete=models.PROTECT)
    user_discord = models.CharField(max_length=500)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_recruta_reprovado'

    def __str__(self):
        return '{}'.format(self.usuario.first_name)
