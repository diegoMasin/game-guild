from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.guerras import Guerras


class ParticiparGuerra(models.Model):
    PARTICIPAR_SIM = 'Sim'
    PARTICIPAR_NAO = 'Não'
    PARTICIPAR_TALVEZ = 'Talvez'
    OPCAO_PARTICIPACAO = (
        (PARTICIPAR_SIM, PARTICIPAR_SIM),
        (PARTICIPAR_TALVEZ, PARTICIPAR_TALVEZ),
        (PARTICIPAR_NAO, PARTICIPAR_NAO),
    )

    id = models.AutoField(primary_key=True)
    guerra = models.ForeignKey(Guerras, on_delete=models.PROTECT)
    participa = models.CharField(choices=OPCAO_PARTICIPACAO, max_length=10, default=PARTICIPAR_SIM)
    participante = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_participar_guerra'

    def __str__(self):
        return '{}-{}-{}'.format(self.guerra, self.participante, self.participa)

    def get_color_participa(self):
        result = ''
        if self.participa == self.PARTICIPAR_SIM:
            result = 'text-success'
        elif self.participa == self.PARTICIPAR_NAO:
            result = 'text-danger'
        elif self.participa == self.PARTICIPAR_TALVEZ:
            result = 'text-warning'
        return result
