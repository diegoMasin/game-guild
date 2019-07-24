from django.db import models

from bdo_gestor_guilda.usuario.models.user_avancado import UserAvancado
from bdo_gestor_guilda.core.models.payout import Payout


class PayoutPersonalizado(models.Model):
    id = models.AutoField(primary_key=True)
    payout = models.ForeignKey(Payout, db_column='fk_payout', on_delete=models.PROTECT)
    usuario = models.ForeignKey(UserAvancado, db_column='fk_user_avancado', on_delete=models.PROTECT)
    tier_adicional = models.IntegerField()

    class Meta:
        db_table = 'tb_payout_personalizado'

    def __str__(self):
        return 'Payout Adicional da Semana: {} - {}'.format(self.payout.data_inicio.strftime('%d/%m/%Y'),
                                                            self.payout.data_fim.strftime('%d/%m/%Y'))
