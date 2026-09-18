from google import genai
import webbrowser
import pyautogui
import schedule
import time
import pyperclip
from urllib.parse import quote
import sys

# ==========================================
# CONFIGURAÇÕES INICIAIS
# ==========================================
CHAVE_API = "SUA_NOVA_CHAVE_AQUI"  # Substitua pela sua chave de API do Google AI

# Lista da rapaziada / contatos
contatos = [
    {"nome": "contato1", "numero": "+558599999999", "apelido": "boneca"},
    {"nome": "contato2", "numero": "+558599999999", "apelido": "princesa"}
]

# Tenta inicializar o cliente da IA. Se der erro de cara (ex: sem internet), ele avisa.
try:
    client = genai.Client(api_key=CHAVE_API)
except Exception as e:
    print(f"⚠️ Aviso: Não foi possível conectar ao Google AI. O robô funcionará apenas com mensagens padrão. Erro: {e}")
    client = None

# ==========================================
# FUNÇÕES DO ROBÔ
# ==========================================
def gerar_mensagem_com_ia(nome, apelido):
    mensagem_emergencia = f"Bom dia, {apelido}! ❤️ Como está hoje?"
    
    # Se o cliente nem iniciou, já pula pra emergência
    if not client or CHAVE_API == "SUA_NOVA_CHAVE_AQUI":
        return mensagem_emergencia

    prompt = f"""
    Escreva uma mensagem curta de bom dia no WhatsApp para a minha namorada {nome}. 
    Eu costumo chamar ela de '{apelido}'.
    Regras:
    - Seja carinhoso, mas descontraído.
    - Não gosto de textão romântico clichê.
    - Máximo de 3 frases e no máximo 2 emojis, nem tooda mensagem precisa ter emojis.
    - Nunca repita a mesma mensagem.
    """
    
    print(f"⏳ Consultando a IA para {nome}...")
    
    try:
        # A chamada para a IA
        resposta = client.models.generate_content(
            model='gemini-3.6-flash', 
            contents=prompt
        )
        return resposta.text.strip() 
        
    except Exception as e:
        # Pega qualquer erro (503 do Google, sem internet, timeout) e trata silenciosamente
        print(f"❌ Falha na IA para {nome} (Erro: {str(e)[:50]}...). Usando mensagem padrão.")
        return mensagem_emergencia

def mandar_bom_dia():
    print("\n🚀 Iniciando a rotina de bom dia de uma chibatada só...")
    
    try:
        print("🌐 Abrindo WhatsApp Web principal...")
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(20) # Tempo para o WhatsApp conectar ao celular
    except Exception as e:
        print(f"❌ Erro crítico ao tentar abrir o navegador: {e}")
        return # Para a execução se o navegador não abrir

    for contato in contatos:
        mensagem = gerar_mensagem_com_ia(contato['nome'], contato['apelido'])
        print(f"💬 Texto gerado: {mensagem}")
        
        mensagem_url = quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={contato['numero']}&text={mensagem_url}"
        
        try:
            # 1. Vai para a barra de endereços
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(1)
            
            # 2. Copia e cola o link (Evita o bug das teclas do Windows)
            pyperclip.copy(link)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1) 
            
            # 3. Dá Enter para carregar o chat
            pyautogui.press('enter')
            
            # 4. Aguarda a tela "Iniciando conversa" sumir
            print(f"🔄 Carregando chat de {contato['nome']}...")
            time.sleep(12) 
            
            # 5. Envia a mensagem
            pyautogui.press('enter')
            print(f"✅ Mensagem enviada com sucesso para {contato['nome']}!\n")
            
            time.sleep(3) # Pausa antes do próximo contato
            
        except Exception as e:
            # Se der erro na automação de UM contato, ele avisa mas NÃO PARA o robô.
            # Ele pula pro próximo da lista!
            print(f"⚠️ Erro ao automatizar a tela para {contato['nome']}: {e}\n")
            
    print("🎉 Rotina finalizada! Todas as mensagens da lista foram processadas.")

# ==========================================
# EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == "__main__":
    try:
        # Para testar imediatamente, deixamos a função ativada:
        mandar_bom_dia()
        
        # O código de agendamento está aqui preparado (descomente quando for botar em produção real):
        schedule.every().day.at("07:30").do(mandar_bom_dia)
        print("🤖 Robô em modo de espera. Aguardando o horário agendado...")
        while True:
            schedule.run_pending()
            time.sleep(60)
            
    except KeyboardInterrupt:
        # Isso captura o seu 'Ctrl + C' e fecha o programa com elegância, sem cuspir erros vermelhos na tela
        print("\n🛑 Robô cancelado pelo usuário (Ctrl + C). Saindo na paz!")
        sys.exit(0)
    except Exception as e:
        # Captura qualquer bizarrice não prevista que derrubaria o sistema inteiro
        print(f"\n💥 Ocorreu um erro fatal inesperado: {e}")