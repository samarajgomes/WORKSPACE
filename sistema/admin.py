from django.contrib import admin
from sistema import models

@admin.register(models.Paciente) # Registrando a classe paciente no Portal do Python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'active',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'crm', 'especialidade', 'active',)

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status',)