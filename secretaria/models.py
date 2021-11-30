from django.db import models
from Pesquisador.models import Protocolo, User


class Encaminhar(models.Model):
    UserProtocolo = models.ForeignKey(User, on_delete=models.PROTECT)
    protocoloEN = models.ManyToManyField(Protocolo)

    def __str__(self):
        return self.UserProtocolo

    def getAvaliador(self):
        return self.User.objects.filter(groups=2)
