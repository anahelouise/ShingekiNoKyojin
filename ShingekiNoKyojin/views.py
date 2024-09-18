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
        <p>Shingeki no Kyojin (Attack on Titan) é um anime e mangá criado por Hajime Isayama. A história se passa em um mundo onde a humanidade vive cercada por enormes muralhas para se proteger de criaturas gigantescas chamadas Titãs, que devoram humanos. A trama segue Eren Jaeger, um jovem cujo objetivo é exterminar os Titãs após presenciar a destruição de sua cidade e a morte de sua mãe durante um ataque.

        Conforme a série avança, os personagens descobrem segredos obscuros sobre os Titãs e a origem da própria humanidade, desvendando uma trama cheia de reviravoltas, ação e mistério. Shingeki no Kyojin é conhecida por seu enredo sombrio, batalhas intensas e questionamentos sobre liberdade, poder e sacrifício.</p>
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
        <p>Levi Ackerman é um dos personagens mais icônicos de Shingeki no Kyojin (Attack on Titan). Ele é o capitão do Esquadrão de Operações Especiais das Tropas de Exploração e é amplamente reconhecido como o soldado mais forte da humanidade. Levi é famoso por suas habilidades extraordinárias em combate contra Titãs e por sua personalidade séria e fria, mas com um forte senso de responsabilidade e dever.
        Sua liderança, habilidade inigualável e história de vida trágica o tornam um dos personagens mais respeitados e admirados dentro do anime</p>
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
