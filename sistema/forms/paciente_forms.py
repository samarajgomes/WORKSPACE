from django import forms
from sistema.models import *

#formulario de paciente (usado para cadastrar e editar)
class PacienteForm(forms.ModelForm):
    "No model Paciente, o CPF tem 11 char, mas aqui podemos aceitar ate 14"
    cpf = forms.CharField (
        max_length=14,
        label="CPF",
)
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf',]
        labels = {
            "nome": "Nome",
            "sobrenome": "Sobrenome",
            "email": "Email",
            "telefone": "Telefone",
            "cpf": "CPF",
        }







