from django.db import models # ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # Util para gerar data/hora atual no projeto


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