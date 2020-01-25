from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_auto_20190924_1420'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe, slug) VALUES ('guardian', 'Guardian');")
    ]
