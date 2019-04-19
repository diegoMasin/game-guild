from django.db import models


class TipoClasseChar(models.Model):
    id = models.AutoField(primary_key=True)
    nome_classe = models.CharField(max_length=50)

    class Meta:
        db_table = 'tb_tipo_classe_char'

    def __str__(self):
        return self.nome_classe
