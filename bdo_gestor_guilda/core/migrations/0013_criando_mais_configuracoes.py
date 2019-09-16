# Generated by Django 2.0.7 on 2019-09-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_migrate_cores'),
    ]

    operations = [
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_string) VALUES (
          'site_guilda', 'Site da Guilda', 0, '');
        '''),
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_inteiro) VALUES (
          'fechamento_war', 'Fechamento das Participações em Guerras', 1, 22);
        '''),
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_inteiro) VALUES (
          'tier_por_node', 'Quantos Tier por Nodewar', 1, 1);
        '''),
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_inteiro) VALUES (
          'tier_por_siege', 'Quantos Tier por Siege', 1, 2);
        '''),
    ]
