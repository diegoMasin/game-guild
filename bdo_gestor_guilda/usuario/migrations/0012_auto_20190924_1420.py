# Generated by Django 2.0.7 on 2019-09-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_acertando_slug_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoclassechar',
            name='nome_classe',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tipoclassechar',
            name='slug',
            field=models.CharField(max_length=50),
        ),
    ]
