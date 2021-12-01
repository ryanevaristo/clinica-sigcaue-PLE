from django.db import models
from Pesquisador.models import Protocolo, User


class Encaminhar(models.Model):
    UserProtocolo = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Selecione o Avaliador:", limit_choices_to={'groups': 2})
    protocoloEN = models.ForeignKey(Protocolo,on_delete=models.PROTECT,verbose_name="Escolha o Protocolo")




