import os

from django.db import models


def get_image_mini_path(instance, filename):
    return os.path.join('logo_classes', str(instance.id), filename)


class TipoClasseChar(models.Model):
    id = models.AutoField(primary_key=True)
    nome_classe = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50)
    # img_mini

    class Meta:
        db_table = 'tb_tipo_classe_char'

    def __str__(self):
        return self.slug
