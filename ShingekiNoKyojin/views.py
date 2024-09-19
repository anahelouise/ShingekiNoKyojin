from django.http import HttpResponse

def index(request):

    return HttpResponse("Esta é a página inicial")

def sobre(request):
    return HttpResponse("Bem-vindo ao Shingeki no Kyojin")

def perfil_usuario(request):
    return HttpResponse("Levi Ackerman, Capitão do Esquadrão de Operações Especiais das Tropas de Exploração")

def contato(request):
    return HttpResponse("Pagina de Contato")

