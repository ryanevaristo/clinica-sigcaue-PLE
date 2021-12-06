# Generated by Django 3.2.7 on 2021-12-06 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pesquisador', '0008_alter_protocolo_status'),
        ('secretaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encaminhar',
            name='UserProtocolo',
            field=models.ForeignKey(limit_choices_to={'groups': 2}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Selecione o Avaliador:'),
        ),
        migrations.AlterField(
            model_name='encaminhar',
            name='protocoloEN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pesquisador.protocolo', verbose_name='Escolha o Protocolo'),
        ),
    ]