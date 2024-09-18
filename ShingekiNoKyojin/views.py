# snk_app/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo ao Shingeki no Kyojin! Esta é a página inicial.")

def sobre(request):
    return HttpResponse("Sobre Shingeki no Kyojin")

def perfil_usuario(request):
    return HttpResponse("Levi Ackerman, Capitão do Esquadrão de Operações Especiais das Tropas de Exploração ")

def contato(request):
    return HttpResponse("Essa é a pagina de contato")
