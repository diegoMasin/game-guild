# Generated by Django 2.0.7 on 2019-04-19 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('CAVALEIRO');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('VALKYRIA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('BERSERKER');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('CACADORA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('ARQUEIRO');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('MAGO');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('BRUXA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('FEITICEIRA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('NINJA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('KUNOICHI');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('MUSA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('MAEHWA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('TAMER');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('MISTICA');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('STRIKER');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('LAHN');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('DARK_KNIGHT');")
    ]
