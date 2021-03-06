# Generated by Django 3.2.7 on 2021-12-08 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0008_alter_protocolo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='status',
            field=models.CharField(blank=True, choices=[('APROVADO', 'APROVADO'), ('REPROVADO', 'REPROVADO'), ('PENDENTE', 'PENDENTE')], default='PENDENTE', max_length=9),
        ),
        migrations.CreateModel(
            name='Emitir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinatura', models.CharField(blank=True, choices=[('Não-assinado', 'Não assinado'), ('Assinado', 'Assinado')], default='Assinado', max_length=12)),
                ('protocoloEM', models.ForeignKey(limit_choices_to={'status': 'APROVADO'}, on_delete=django.db.models.deletion.CASCADE, to='Pesquisador.protocolo', verbose_name='Escolha o Protocolo')),
            ],
        ),
    ]
