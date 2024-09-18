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
    html = """
    <html>
    <head><title>Sobre Shingeki no Kyojin</title></head>
    <body>
        <h1>Sobre Shingeki no Kyojin</h1>
        <p>Shingeki no Kyojin (Attack on Titan) é um anime e mangá criado por Hajime Isayama.
    </body>
    </html>
    """
    return HttpResponse(html)

def perfil_usuario(request):
    html = """
    <html>
    <head><title>Perfil de Usuário</title></head>
    <body>
        <h1>Perfil de Levi Ackerman</h1>
        <ul>
            <li>Nome: Levi Ackerman</li>
            <li>Regimento: Capitão do Esquadrão de Operações Especiais das Tropas de Exploração</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

def contato(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        html = f"""
        <html>
        <head><title>Contato</title></head>
        <body>
            <h1>Contato</h1>
            <p>Mensagem enviada: {mensagem}</p>
        </body>
        </html>
        """
        return HttpResponse(html)
    
    html = """
    <html>
    <head><title>Contato</title></head>
    <body>
        <h1>Contato</h1>
        <form method='POST'>
            <label for='mensagem'>Sua mensagem:</label>
            <textarea id='mensagem' name='mensagem'></textarea>
            <button type='submit'>Enviar</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)
