from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# VIEWS -> sempre retornam algo; são funções. request -> response
# View responsavel pela tela inicial do médico
def medico_view(request):
    print('Página consulta funcionou')
    return  HttpResponse('Página inicial da consulta') #def Obrigatoriamente retorna a alguma coisa




