from django.db import models


class Payout(models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    url_print_payout = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'tb_payout'

    def __str__(self):
        return 'Payout da Semana: {} - {}'.format(self.data_inicio.strftime('%d/%m/%Y'),
                                                  self.data_fim.strftime('%d/%m/%Y'))

    def get_url_print_payout(self):
        url = self.url_print_payout
        if not ('http://' in url or 'https://' in url):
            url = 'http://{0}'.format(url)
        return url
