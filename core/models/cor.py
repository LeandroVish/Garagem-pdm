from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} {self.id}"