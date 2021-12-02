# Generated by Django 3.2.7 on 2021-12-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_avaliador',
            field=models.BooleanField(blank=True, null=True, verbose_name='É Avaliador ?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_presidente',
            field=models.BooleanField(blank=True, verbose_name='É presidente ?'),
        ),
    ]