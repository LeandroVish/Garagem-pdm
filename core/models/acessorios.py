from django.db import models

class Acessorios(models.Model):
    descricao = models.CharField(max_lenght=200)

    def __str__(self):
        return self.nome