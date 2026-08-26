from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Util para gerar data/hora atual no projeto

# Modelo que representa um Paciente.
# atributo => nome, sobrenome, email, telefone, data de cadastro, mensagem, active (True/False)

class Paciente (models.Model):
    nome = models.CharField(max_length=25) ## o quantitativo de caracteres que pode ter
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField() ## campo de email
    telefone = models.CharField(max_length=15)
    criacao_data = models.DateTimeField(default=timezone.now) ## Pega o fuso horario atual e a data de hoje
    mensagem = models.TextField(blank=True) # Ela pode ficar em branco; não é obrigatório
    active = models.BooleanField(default=True)