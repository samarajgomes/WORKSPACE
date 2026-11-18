from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# VIEWS -> sempre retornam algo; são funções. request -> response
# View responsavel pela tela inicial do médico
def medico_view(request):
    print('Página médico funcionou')
    return  HttpResponse('Página inicial do Médico') #def Obrigatoriamente retorna a alguma coisa




