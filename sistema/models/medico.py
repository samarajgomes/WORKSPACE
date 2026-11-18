from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Util para gerar data/hora atual no projeto


class Medico (models.Model):
    nome = models.CharField(max_length=25) 
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField() 
    data_criacao = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    mensagem = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}' # Retorna uma string com o nome, sobrenome
