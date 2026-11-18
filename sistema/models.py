from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Util para gerar data/hora atual no projeto

# Modelo que representa um Paciente.
# atributo => nome, sobrenome, email, telefone, data de cadastro, mensagem, active (True/False)

class Paciente (models.Model):
    nome = models.CharField(max_length=25) ## max_length --> o quantitativo de caracteres que pode ter
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField() ## campo de email
    telefone = models.CharField(max_length=15) 
    cpf =  models.CharField(max_length=11) #CPF com 11 digitos, sem traço e ponto
    criacao_data = models.DateTimeField(default=timezone.now) ## Pega o fuso horario atual e a data de hoje
    mensagem = models.TextField(blank=True) # Ela pode ficar em branco; não é obrigatório
    active = models.BooleanField(default=True) # Campo de exclusão lógica, caso o paciente seja desativado, não será excluido do banco de dados, apenas marcado como inativo

    # criando função
    def __str__(self):
        return f'{self.nome} {self.sobrenome}' # vou acessar o nome e o sobrenome do paciente q esta sendo criado. Nao tem a ver com Banco de Dados, mas sim administração do Django


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

# Modelo que representa uma consulta
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