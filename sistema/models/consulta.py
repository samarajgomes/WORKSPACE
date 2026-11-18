from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Util para gerar data/hora atual no projeto


class Consulta (models.Model):
  paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # chave estrangeira
  medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # chave estrangeira
  data_consulta = models.DateTimeField(default=timezone.now) # Data/hora da consulta
  active = models.BooleanField(default=True) # Campo de exclusão Lógica
  observacao = models.TextField(blank=True) # Anotação opcional
  status = models.CharField(
      default='A',
      max_length=1,
      choices=[
          ('A', 'Agendada'),
          ('X', 'Cancelada'),
          ('C', 'Confirmada'),
          ('R', 'Realizada'),
      ]
  )