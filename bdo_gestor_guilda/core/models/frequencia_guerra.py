from django.contrib.postgres.fields import ArrayField
from django.db import models

from bdo_gestor_guilda.core.models.guerras import Guerras


class FrequenciaGuerra(models.Model):
    id = models.AutoField(primary_key=True)
    guerra = models.ForeignKey(Guerras, on_delete=models.PROTECT, )
    participantes = ArrayField(ArrayField(models.IntegerField()))

    class Meta:
        db_table = 'tb_frequencia_guerra'

    def __str__(self):
        return self.guerra
