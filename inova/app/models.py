from django.db import models

class ClassiFinDtNotific(models.Model):  # Correção: herdar de models.Model
    id_dengue01 = models.AutoField(primary_key=True)
    dt_notific = models.DateField()
    classi_fin = models.CharField(max_length=255)  # Adicione um max_length
    quantidade = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id_dengue01}, Data: {self.dt_notific}, Classificação: {self.classi_fin}, Quantidade: {self.quantidade}"


