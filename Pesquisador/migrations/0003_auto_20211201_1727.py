# Generated by Django 3.2.7 on 2021-12-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0002_auto_20211201_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_avaliador',
            field=models.BooleanField(null=True, verbose_name='É Avaliador ?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_presidente',
            field=models.BooleanField(verbose_name='É presidente ?'),
        ),
    ]