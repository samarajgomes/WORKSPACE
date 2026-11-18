from django.urls import path
from sistema.VIEWS import medico_view

urlpatterns = [
    path('medico/', medico_view), # vollmed.com/medico
    path('medico/novo/'),  # vollmed.com/medico/novo/
    path('medico/perfil/<int:medico_id>'),  # vollmed.com/medico/perfil
    path('medico/listagem') # vollmed.com/medico/listagem
]