# Generated by Django 3.2.7 on 2021-12-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0003_auto_20211201_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(),
        ),
    ]