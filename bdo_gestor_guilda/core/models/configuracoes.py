from django.db import models


class Configuracoes(models.Model):
    STRING_ID = 0
    INTEIRO_ID = 1
    BOOL_ID = 2
    TIPO_VARIAVEL = (
        (STRING_ID, 'String'),
        (INTEIRO_ID, 'Inteiro'),
        (BOOL_ID, 'Booleano'),
    )
    NOME_VARIAVEL_SITE_GUILDA = 'site_guilda'

    id = models.AutoField(primary_key=True)
    nome_variavel = models.CharField(max_length=100)
    slug_variavel = models.CharField(max_length=200)
    tipo_variavel = models.IntegerField(choices=TIPO_VARIAVEL)
    valor_inteiro = models.IntegerField(null=True, blank=True)
    valor_string = models.CharField(max_length=100, null=True, blank=True)
    valor_bool = models.NullBooleanField(null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    data_atualizacao = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_configuracoes'

    def __str__(self):
        return '{}'.format(self.nome_variavel)
