import tkinter as tk

class BlinkingText:
    def __init__(self, janela, texto_inicial, intervalo, **kwargs):
        self.janela = janela
        self.texto_inicial = texto_inicial
        self.intervalo = intervalo
        self.label = tk.Label(janela, text=self.texto_inicial, **kwargs)
        self.label.pack(pady=10)
        self.blink()

    def blink(self):
        current_text = self.label.cget("text")
        if current_text.endswith("█"):
            self.label.config(text=self.texto_inicial + " ")  # Remove o █
        else:
            self.label.config(text=self.texto_inicial + "█")  # Adiciona o █

        # Chama a função novamente após o intervalo
        self.janela.after(self.intervalo, self.blink)

def criar_janela():
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


     # Criar outro texto estático (exemplo)
    texto_adicional = "Meu nome é Lina, e eu guiarei sua jornada!"
    label_texto_adicional = tk.Label(janela, text=texto_adicional, font=("Courier", 12), fg="green", bg="black")
    label_texto_adicional.pack(pady=10)

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



    # Função para abrir a nova janela e fechar a atual
    def iniciar_proxima_janela(event):
        janela.destroy()  # Fecha a janela atual
        criar_segunda_janela()  # Abre a nova janela

    # Ativar evento de teclado para abrir a nova janela
    janela.bind("<Key>", iniciar_proxima_janela)

    # Iniciar a janela
    janela.mainloop()

def criar_segunda_janela():
    # Função para criar a nova janela
    nova_janela = tk.Tk()
    nova_janela.title("Nova Fase")
    nova_janela.configure(bg="black")
    nova_janela.state('zoomed')

    # Texto na nova janela
    label = tk.Label(
        nova_janela,
        text="Bem-vindo à próxima etapa!",
        font=("Courier", 12),
        fg="green",
        bg="black"
    )
    label.pack(pady=100)

    nova_janela.mainloop()



criar_janela()