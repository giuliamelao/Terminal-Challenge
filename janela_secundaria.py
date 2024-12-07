import tkinter as tk

def criar_segunda_janela():
    # Criar a nova janela
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
