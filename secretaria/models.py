from django.db import models
from Pesquisador.models import Parecer, User, Protocolo


class Encaminhar(models.Model):
    UserProtocolo = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Selecione o Avaliador:", limit_choices_to={'groups': 2})
    protocoloEN = models.ForeignKey(Protocolo,on_delete=models.CASCADE,verbose_name="Escolha o Protocolo",limit_choices_to={'status': 'PENDENTE'})




class EncaminharAP(models.Model):
    UserProtocolo = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Selecione o Presidente:", limit_choices_to={'groups': 4})
    protocoloEN = models.ForeignKey(Parecer,on_delete=models.CASCADE,verbose_name="Escolha o Protocolo",limit_choices_to={'status': 'Recomendado'})