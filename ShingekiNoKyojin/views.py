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
        <p>Shingeki no Kyojin, conhecido como "Attack on Titan" em inglês, é um anime e mangá criado por Hajime Isayama, Que se passa em um mundo onde a humanidade vive em cidades cercadas por enormes muralhas para se proteger dos Titãs, criaturas gigantes que devoram humanos.</p>
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
            <li>Gênero: Masculino</li>
            <li>Idade: Pelo menos 30 anos</li>
            <li>Regimento: Capitão do Esquadrão de Operações Especiais das Tropas de Exploração</li>
            <li>Abates de Titãs: Pelo menos 89</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

def contato(request):
    if request.method == 'POST':
        regimento = request.POST.get('regimento')
        mensagem = request.POST.get('mensagem')
        html = f"""
        <html>
        <head><title>Contato</title></head>
        <body>
            <h1>Contato</h1>
            <p>Você escolheu se alistar no regimento: {regimento}</p>
            <p>Sua mensagem: {mensagem}</p>
        </body>
        </html>
        """
        return HttpResponse(html)
   
    html = """
    <html>
    <head><title>Contato</title></head>
    <body>
        <h1>Contato</h1>
            <label for='mensagem'>Entre em contato:</label>
            <textarea id='mensagem' name='mensagem' rows='4' cols='50'></textarea>
            <br><br>
            <button type='submit'>Enviar</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)

