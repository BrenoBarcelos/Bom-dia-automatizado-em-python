# 🤖 BomDiaPython - O Robô do "Bom dia, amor!" (Da Chibatada Só)

Você já acordou na correria e esqueceu de mandar o sagrado "Bom dia" pra gata (ou pras gatas)? Seus problemas acabaram! 

O **BomDiaPython** é um script de automação 100% Python que abre o WhatsApp Web e faz o trabalho duro por você. E o melhor: equipado com a IA do **Google Gemini (3.6-Flash)** para gerar mensagens diárias únicas, com a sua personalidade e as suas gírias, garantindo que o seu "suave" e "tranquilo" cheguem intactos, sem parecer um robô sem alma.

## 🚀 Como a mágica acontece (A técnica da "Chibatada Só")
Nas primeiras versões, o robô abria e fechava uma aba do navegador para cada pessoa. Feio, pesado e amador.

Refatoramos a arquitetura para o método **"De uma chibatada só"**:
1. O robô abre o WhatsApp Web principal apenas UMA vez.
2. A IA gera todas as mensagens baseadas em um Prompt dinâmico de personalidade.
3. Usando `pyautogui` e `pyperclip` (para burlar o famoso bug de caracteres da barra de endereços do Windows), o robô injeta o link via **Ctrl+L** e **Ctrl+V**, navegando entre os contatos na mesma aba sem recarregar a página!
4. **Resiliência Pura:** Se a internet cair, o servidor do Google engasgar (Erro 503) ou alguém cancelar no meio (o bom e velho `Ctrl+C`), nosso bloco `try/except` assume o volante e garante o envio de mensagens de emergência. A chibatada não para!

## ⚙️ Tecnologias Utilizadas
* `Python` (O coração da fera)
* `google-genai` (Acessando o modelo mais atual Gemini 3.6-Flash)
* `pyautogui` & `pyperclip` (Nossos estagiários que controlam o teclado de forma veloz)
* `schedule` (Pra acordar mais cedo que você e trabalhar)
* `webbrowser` (Pra injetar as URLs no navegador padrão)

## 🛠️ Como rodar na sua máquina

**1. Clone e crie o ambiente virtual (Melhor prática, né pai?)**
```bash
git clone [https://github.com/SeuUsuario/bomdiapython.git](https://github.com/SeuUsuario/bomdiapython.git)
cd bomdiapython
python -m venv .venv
source .venv/Scripts/activate # No Windows (Git Bash)
