import tkinter as tk
from janela_secundaria import criar_segunda_janela
from utils import BlinkingText

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
    label_texto_estatico = tk.Label(janela, text=texto_estatico, font=("Courier", 12), fg="green", bg="black")
    label_texto_estatico.pack(pady=20)

    # Texto adicional
    texto_adicional = "Meu nome é Lina, e eu guiarei sua jornada!"
    label_texto_adicional = tk.Label(janela, text=texto_adicional, font=("Courier", 12), fg="green", bg="black")
    label_texto_adicional.pack(pady=10)

    # Texto estático "Bem-vindo"
    texto_iniciar = "Bem-vindo ao Terminal Challenge!"
    label_iniciar = tk.Label(janela, text=texto_iniciar, font=("Courier", 12), fg="green", bg="black")
    label_iniciar.pack(pady=10)

    # Adicionar o texto que pisca
    blinking_text = BlinkingText(
        janela,
        "Pressione qualquer tecla para iniciar...\n",
        500,
        font=("Courier", 12),
        fg="green",
        bg="black"
    )

    # Função para abrir a próxima janela
    def iniciar_proxima_janela(event):
        janela.destroy()
        criar_segunda_janela()

    # Ativar evento de teclado
    janela.bind("<Key>", iniciar_proxima_janela)

    # Iniciar janela
    janela.mainloop()
