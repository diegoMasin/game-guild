from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class Guerras(models.Model):
    TIPO_NODEWAR_ID = 1
    TIPO_SIEGE_ID = 2
    TIPO_NODEWAR_SLUG = 'Nodewar'
    TIPO_SIEGE_SLUG = 'Siege'
    TIPOS = (
        (TIPO_NODEWAR_ID, TIPO_NODEWAR_SLUG),
        (TIPO_SIEGE_ID, TIPO_SIEGE_SLUG),
    )
    MODELO_OFICIAL_ID = 1
    MODELO_4FUN_ID = 2
    MODELO_OFICIAL_SLUG = 'Oficial'
    MODELO_4FUN_SLUG = '4Fun'
    MODELOS = (
        (MODELO_OFICIAL_ID, MODELO_OFICIAL_SLUG),
        (MODELO_4FUN_ID, MODELO_4FUN_SLUG),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.IntegerField(choices=TIPOS, default=TIPO_NODEWAR_ID)
    modelo = models.IntegerField(choices=MODELOS, default=MODELO_OFICIAL_ID)
    data_inicio = models.DateField()
    call = models.ForeignKey(UserAvancado, db_column='call_user_avancado', on_delete=models.PROTECT,
                             null=True, blank=True)
    pt_fixa = models.BooleanField(default=True)
    quantidade_players = models.IntegerField(blank=True, null=True)
    servidor = models.CharField(max_length=50, blank=True, null=True)
    node = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'tb_guerras'

    def __str__(self):
        return '{}'.format(self.data_inicio)

    def get_membros(self):
        from bdo_gestor_guilda.core.models.vinculo_grupos import VinculoGrupos
        return VinculoGrupos.objects.filter(grupo=self).order_by('membro')

    def get_slug_tipo(self):
        tipo = ''
        if self.tipo == self.TIPO_NODEWAR_ID:
            tipo = self.TIPO_NODEWAR_SLUG
        if self.tipo == self.TIPO_SIEGE_ID:
            tipo = self.TIPO_SIEGE_SLUG
        return tipo

    def get_slug_modelo(self):
        modelo = ''
        if self.modelo == self.MODELO_OFICIAL_ID:
            modelo = self.MODELO_OFICIAL_SLUG
        if self.modelo == self.MODELO_4FUN_ID:
            modelo = self.MODELO_4FUN_SLUG
        return modelo
