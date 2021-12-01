# Generated by Django 3.2.7 on 2021-12-01 20:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bioterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bioterio', models.CharField(max_length=100, verbose_name='Bioterio')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPJ')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(max_length=100, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Municipio')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome: ')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('idade', models.CharField(blank=True, max_length=3, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF')),
                ('universidade', models.CharField(max_length=100, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False)),
                ('is_avaliador', models.BooleanField(blank=True, default=False, null=True, verbose_name='É Avaliador ?')),
                ('is_presidente', models.BooleanField(blank=True, default=False, verbose_name='É presidente ?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_protocolo', models.CharField(max_length=100, null=True, verbose_name='Titulo')),
                ('justificativa', models.CharField(max_length=100, verbose_name='Justificativa')),
                ('resumo', models.TextField(verbose_name='Resumo em Português')),
                ('resumo_en', models.TextField(verbose_name='Resumo em Inglês')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_termino', models.DateField(verbose_name='Data de Termino')),
                ('especie', models.CharField(max_length=50, verbose_name='Espécie')),
                ('quantidade', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('AP', 'APROVADO'), ('RE', 'REPROVADO'), ('PE', 'PENDENTE')], default='PE', max_length=2)),
                ('bioterio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pesquisador.bioterio')),
            ],
        ),
    ]
