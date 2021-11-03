from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100,null=True)
    idade = models.CharField(max_length=3,null=True)
    cpf = models.CharField(max_length=14 ,verbose_name='CPF',null=True)
    universidade = models.CharField(max_length=100,null=True)


class Protocolo(models.Model):


    STATUS_CHOICES = [
    ('AP', 'APROVADO'),
    ('RE', 'REPROVADO'),
    ('PE', 'PENDENTE'),
]

    titulo_protocolo = models.CharField('Titulo', max_length=100, null=True)
    justificativa = models.CharField('Justificativa',max_length=100)
    resumo = models.TextField("Resumo em Português")
    resumo_en = models.TextField("Resumo em Inglês")
    data_inicio = models.DateField("Data de Início")
    data_termino = models.DateField("Data de Termino")
    especie = models.CharField("Espécie", max_length=50)
    quantidade = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')

    def __str__(self):
        return self.titulo_protocolo

class Bioterio(models.Model):

    nome_bioterio = models.CharField('Bioterio', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=100)
    rua = models.CharField('Rua', max_length=100)
    numero = models.CharField('Número', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Municipio', max_length=100)
    estado = models.CharField('Estado', max_length=100)

    def __str__(self):
        return self.nome_bioterio       