# snk_app/views.py

from django.http import HttpResponse

def index(request):
    html = """
    <html>
    <head><title>Página Inicial</title></head>
    <body>
        <h1>Bem-vindo ao Shingeki no Kyojin!</h1>
        <p>Esta é a página inicial.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def sobre(request):
    return HttpResponse("Sobre Shingeki no Kyojin")

def perfil_usuario(request):
    return HttpResponse("Levi Ackerman, Capitão do Esquadrão de Operações Especiais das Tropas de Exploração ")

def contato(request):
    return HttpResponse("Essa é a pagina de contato")
