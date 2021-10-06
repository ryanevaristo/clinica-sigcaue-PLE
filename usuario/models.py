from django.db import models

# Create your models here.


class Protocolo(models.Model):


    STATUS_CHOICES = [
    ('AP', 'APROVADO'),
    ('RE', 'REPROVADO'),
    ('PE', 'PENDENTE'),
]

    justificativa = models.CharField('Justificativa',max_length=100)
    resumo = models.TextField("Resumo em Português")
    resumo_en = models.TextField("Resumo em Inglês")
    data_inicio = models.DateField("Data de Início")
    data_termino = models.DateField("Data de Termino")
    especie = models.CharField("Espécie", max_length=50)
    quantidade = models.IntegerField()
    bioterio = models.CharField("Biotério", max_length=50)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')

    def __str__(self):
        return self.bioterio