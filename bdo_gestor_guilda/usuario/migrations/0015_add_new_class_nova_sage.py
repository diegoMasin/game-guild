# Generated by Django 2.0.7 on 2021-03-16 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_add_new_classe_hashashin'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe, slug) VALUES ('nova', 'Nova');"),
        migrations.RunSQL("INSERT INTO tb_tipo_classe_char (nome_classe, slug) VALUES ('sage', 'Sage');")
    ]
