# Generated by Django 2.0.7 on 2019-04-19 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('cavaleiro');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('valkyria');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('berserker');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('cacadora');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('arqueiro');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('mago');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('bruxa');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('feiticeira');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('ninja');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('kunoichi');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('musa');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('maehwa');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('tamer');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('mistica');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('striker');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('lahn');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe) VALUES ('dark_knight');")
    ]
