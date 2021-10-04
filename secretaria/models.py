from django.db import models


class Protocolo(models.Model):
    justificativa = models.CharField('Justificativa',max_length=100)
    resumo = models.TextField("Resumo em Português")
    resumo_en = models.TextField("Resumo em Inglês")
    data_inicio = models.DateField("Data de Início")
    data_termino = models.DateField("Data de Termino")
    especie = models.CharField("Espécie", max_length=50)
    quantidade = models.IntegerField()
    bioterio = models.CharField("Biotério", max_length=50)

    def __str__(self):
        return self.bioterio
