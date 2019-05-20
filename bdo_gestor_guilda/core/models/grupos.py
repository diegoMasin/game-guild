from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class Grupos(models.Model):
    NODEWAR_ID = 1
    SIEGE_ID = 2
    NODEWAR_SLUG = 'Node War'
    SIEGE_SLUG = 'Siege'
    TIPO_GUERRA = (
        ('', 'Selecione uma Opção'),
        (NODEWAR_ID, NODEWAR_SLUG),
        (SIEGE_ID, SIEGE_SLUG)
    )

    id = models.AutoField(primary_key=True)
    lider = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    tipo_guerra = models.IntegerField(choices=TIPO_GUERRA, blank=True, null=True)
    data_cadastro = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'tb_grupos'

    def __str__(self):
        if self.tipo_guerra:
            return '{} - {}'.format(self.titulo, self.tipo_guerra)
        return '{}'.format(self.titulo)

    def get_tipo_guerra(self):
        nome = ''
        if self.tipo_guerra == self.NODEWAR_ID:
            nome = self.NODEWAR_SLUG
        if self.tipo_guerra == self.SIEGE_ID:
            nome = self.SIEGE_SLUG
        return nome
