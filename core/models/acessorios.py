from django.db import models

class Acessorios(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.descricao} {self.id}"