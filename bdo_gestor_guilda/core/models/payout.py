from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado


class Payout(models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    class Meta:
        db_table = 'tb_payout'

    def __str__(self):
        return 'Payout da Semana: {} - {}'.format(self.data_inicio.strftime('%d/%m/%Y'),
                                                  self.data_fim.strftime('%d/%m/%Y'))
