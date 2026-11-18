from django.urls import path
from sistema.VIEWS import *

urlpatterns = [
    path('paciente/', index_paciente), # vollmed.com/paciente
    # path('paciente/novo/'),  # vollmed.com/paciente/novo/
    # path('paciente/perfil/<int:paciente_id>'),  # vollmed.com/paciente/perfil
    # path('paciente/listar_pacientes') # vollmed.com/paciente/listagem
]
# path variable