# Generated by Django 3.2.7 on 2021-12-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0007_auto_20211201_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='status',
            field=models.CharField(blank=True, choices=[('APROVADO', 'APROVADO'), ('REPROVADO', 'REPROVADO'), ('PENDENTE', 'PENDENTE')], default='PE', max_length=9),
        ),
    ]