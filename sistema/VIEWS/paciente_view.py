from django.shortcuts import render
# from django.http import HttpResponse
from sistema.models import Paciente

# Create your views here.
# VIEWS -> sempre retornam algo; são funções. request -> response
# View responsavel pela tela inicial do médico
def index_paciente (request):
    return render(
        request,
        'index.html',
    )

#   Delegar ao agente
    # View responsavel por listar todos os pacientes
    # def listar_pacientes(request):
    #     pacientes =  Paciente.objects.all() # -> (obj1, obj2, obj3)

    #     context = {
    #         'pacientes': pacientes,
    #     }

    #     return render(
    #         request,
    #         'paciente/listar.html',
    #         context,
    #     )














# GLOBAL -> A uma página inteira
# PARTICALS -> Uma parte sda página (header, footer, formulario)

# SPA

# INT -> template/global/base.html




