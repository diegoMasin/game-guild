# Generated by Django 2.0.7 on 2019-05-18 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_recrutareprovado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recrutareprovado',
            old_name='user_discord',
            new_name='justificativa',
        ),
    ]
