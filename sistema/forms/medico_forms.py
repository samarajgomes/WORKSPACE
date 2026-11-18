from django import forms
from sistema.models import *

# Checagem de e-mail -> O EmailField do model já valida se é e-mail válido
# Checagem de dado inserido -> Dependendo o Field do atributo

ESPECIALIDADES = [
    ('CARDIOLOGIA', 'Cardiologia'),
    ('DERMATOLOGIA', 'Dermatologia'),
    ('GINECOLOGIA', 'Ginecologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('OFTAMOLOGIA', 'Oftamologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]

# Formulario do Médico (usado para cadastro e edição)
class MedicoForm(forms.ModelForm):
    # Troca o Charfield padrão por um <select> com opções fixas
    especialidade = forms.ChoiceField(
        choices =[('','Selecioe uma especialidade')] + ESPECIALIDADES,
        label ='Especialidade'
    )

    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'telefone', 'crm', 'especialidade']
        # criacao_data e ativo não aparecem: são preenchidos automaticamente
        labeks = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            "email": 'Email',
            'telefone': 'Telefone',
            'crm': 'CRM',
        }

    
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'mensagem']

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'Email',
            'telefone': 'Telefone',
            'cpf': 'CPF',
            'mensagem': 'Mensagem',
        }

   
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['paciente_id', 'medico_id', 'data_consulta', 'status', 'observacao']

        labels = {
            'paciente_id': 'Paciente',
            'medico_id': 'Médico',
            'data_consulta': 'Data da Consulta',
            'status': 'Status',
            'observacao': 'Observação',
        }

