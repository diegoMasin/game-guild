# Generated by Django 2.0.7 on 2019-08-09 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_configuracoes'),
    ]

    operations = [
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_string) VALUES (
          'nome_guilda', 'Nome da Guilda', 0, 'Coloque_o_nome_da_sua_guilda');
        '''),
        migrations.RunSQL('''
          INSERT INTO tb_configuracoes (nome_variavel, slug_variavel, tipo_variavel, valor_string) VALUES (
          'nome_jogo', 'Nome do Jogo', 0, 'Coloque_o_nome_do_jogo');
        ''')
    ]
