# Generated by Django 3.2.7 on 2021-11-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0006_alter_protocolo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
