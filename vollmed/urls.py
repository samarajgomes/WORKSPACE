
from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
]


# MVT (MVC)



# www.vollmed.online/ 
# www.vollmed.online/login
# www.vollmed.online/ 

# MEDICO
# www.vollmed.online/medico/id -> Perfil do médico 
# www.vollmed.online/medico/id/alterar -> Alterar cadastro do médico

# www.vollmed.online/medico/id/consultas


# PACIENTE
# www.vollmed.online/paciente/id -> Perfil do paciente 
# www.vollmed.online/paciente/id/alterar -> Alterar cadastro do paciente

# www.vollmed.online/paciente/id/consultas/cadastrar/
# www.vollmed.online/paciente/id/consultas/id/ -> ver, alterar, deletar.


# SECRETARIO/SUPERUSUARIO  **se ele é superusuario, ele tem acesso a uma pagina que ninguem mais tem
# www.vollmed.online/secretario/id -> Perfil do secretario 
# www.vollmed.online/secretario/id/alterar -> Alterar cadastro do secretario

# www.vollmed.online/secretario/id/consultas/cadastrar/
# www.vollmed.online/secretario/id/consultas/id/ -> ver, alterar, deletar.


# CONSULTA
