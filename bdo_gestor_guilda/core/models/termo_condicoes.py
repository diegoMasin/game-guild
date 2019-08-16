from django.db import models


class TermoCondicoes(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_termo_condicoes'

    def __str__(self):
        return 'Termo e Condições da Guilda'
