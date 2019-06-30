from django.db import models


class TipoClasseChar(models.Model):
    id = models.AutoField(primary_key=True)
    nome_classe = models.CharField(max_length=50)

    class Meta:
        db_table = 'tb_tipo_classe_char'

    def __str__(self):
        return self.get_slug()

    def get_slug(self):
        slug = ''
        if self.nome_classe == 'cavaleiro':
            slug = 'Cavaleiro'
        if self.nome_classe == 'valkyria':
            slug = 'Valkyria'
        if self.nome_classe == 'berserker':
            slug = 'Berserker'
        if self.nome_classe == 'cacadora':
            slug = 'Caçadora'
        if self.nome_classe == 'arqueiro':
            slug = 'Arqueiro'
        if self.nome_classe == 'mago':
            slug = 'Mago'
        if self.nome_classe == 'bruxa':
            slug = 'Bruxa'
        if self.nome_classe == 'feiticeira':
            slug = 'Feiticeira'
        if self.nome_classe == 'ninja':
            slug = 'Ninja'
        if self.nome_classe == 'kunoichi':
            slug = 'Kunoichi'
        if self.nome_classe == 'musa':
            slug = 'Musa'
        if self.nome_classe == 'maehwa':
            slug = 'Maehwa'
        if self.nome_classe == 'tamer':
            slug = 'Tamer'
        if self.nome_classe == 'mistica':
            slug = 'Mística'
        if self.nome_classe == 'mistica':
            slug = 'Mística'
        if self.nome_classe == 'striker':
            slug = 'Lutador'
        if self.nome_classe == 'lahn':
            slug = 'Lahn'
        if self.nome_classe == 'dark_knight':
            slug = 'Cavaleira das Trevas'
        if self.nome_classe == 'shai':
            slug = 'Shai'
        return slug
