# Generated by Django 3.2.7 on 2021-11-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0002_auto_20211103_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_avaliador',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_presidente',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='idade',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
