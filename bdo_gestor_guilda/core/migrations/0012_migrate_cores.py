# Generated by Django 2.0.7 on 2019-09-13 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_create_termo_condicoes_default'),
    ]

    operations = [
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_string) VALUES (
          'cor_topo', 'Cor do Topo', 0, '#000000');
        '''),
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_string) VALUES (
          'cor_lateral', 'Cor da Lateral', 0, '#660000');
        '''),
    ]
