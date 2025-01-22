import tkinter as tk
import json
from windows.janela_secundaria import criar_segunda_janela
from utils import BlinkingText

def salvar_nome(janela, entrada_nome):
    nome = entrada_nome.get()  # Pega o texto digitado
    dados = {"nome": nome}  # Cria o dicionário com o nome
    
    # Salva no arquivo JSON
    with open("data/usuario.json", "w") as arquivo:
        json.dump(dados, arquivo)
    
    print(f"Nome salvo: {nome}")  # Apenas para feedback no console

    # Exibe a mensagem com o nome do usuário
    mensagem_label = tk.Label(janela, text=f"Muito bem, {nome}! Aperte Espaço e nós iremos na próxima página onde começaremos!", 
                              font=("Courier", 14), fg="#50C878", bg="black")
    mensagem_label.pack(pady=10)


def criar_janela_inicial():
    janela = tk.Tk()
    janela.title("Terminal Challenge")
    janela.configure(bg='black')
    janela.state('zoomed')

    # Criar o texto no estilo de blocos
    texto_estatico = """
    ████████╗   ███████╗
    ╚══██╔══╝   ██╔════╝
  ██║      ██║
   ██║      ██║ 
       ██║      ███████╗
       ╚═╝      ╚══════╝
    """
    label_texto_estatico = tk.Label(janela, text=texto_estatico, font=("Courier", 14), fg="#50C878", bg="black")
    label_texto_estatico.pack(pady=20)

    # Texto adicional
    texto_adicional = "Meu nome é Lina, e eu guiarei sua jornada!"
    label_texto_adicional = tk.Label(janela, text=texto_adicional, font=("Courier", 14), fg="#50C878", bg="black")
    label_texto_adicional.pack(pady=10)

    # Texto estático "Bem-vindo"
    texto_iniciar = "Bem-vindo ao Terminal Challenge!"
    label_iniciar = tk.Label(janela, text=texto_iniciar, font=("Courier", 14), fg="#50C878", bg="black")
    label_iniciar.pack(pady=10)

    # Adicionar entrada para o nome
    label_nome = tk.Label(janela, text="Digite seu nome:", font=("Courier", 14), fg="#50C878", bg="black")
    label_nome.pack(pady=10)

    entrada_nome = tk.Entry(janela, font=("Courier", 12), fg="#50C878", bg="black", insertbackground="white", highlightthickness=0, bd=0)
    entrada_nome.pack(pady=10)
    entrada_nome.focus_set()

    # Ativar a função ao pressionar Enter
    janela.bind("<Return>", lambda event: salvar_nome(janela, entrada_nome))


    # Função para abrir a próxima janela
    def iniciar_proxima_janela(event):
        janela.destroy()
        criar_segunda_janela()

    # Ativar evento de teclado
    janela.bind("<KeyPress-space>", iniciar_proxima_janela)

    # Iniciar janela
    janela.mainloop()    
