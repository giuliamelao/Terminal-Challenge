import tkinter as tk
import json

def carregar_usuario():
    # Carregar o nome do usuário de um arquivo JSON
    with open('data/usuario.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados["nome"]

def carregar_explicacao(fase, comando):
    with open('levels/explicacao.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        # Filtra pela fase e comando
        for explicacao in dados["explicacao"]:
            if explicacao["comando"] == comando:
                return explicacao["texto"]
    return "Texto não encontrado."

def exibir_texto_dinamicamente(label, texto, indice=0, delay=50):
    if indice < len(texto):
        label.config(text=texto[:indice+1])  # Exibe uma letra a mais a cada chamada
        label.after(delay, exibir_texto_dinamicamente, label, texto, indice + 1, delay)

def criar_segunda_janela():
    # Criar a nova janela
    nova_janela = tk.Tk()
    nova_janela.title("Nova Fase")
    nova_janela.configure(bg="black")
    nova_janela.state('zoomed')
    
    # Carregar o nome do usuário
    nome_usuario = carregar_usuario()

    # Carregar o texto da fase 1 e comando pwd
    texto_fase_1_pwd = carregar_explicacao(1, "pwd")

    # Substituir <usuario> pelo nome real
    texto_fase_1_pwd = texto_fase_1_pwd.replace("<usuario>", nome_usuario)

    # Texto na nova janela
    label = tk.Label(
        nova_janela,
        text="",
        font=("Courier", 14),
        fg="#50C878",
        bg="black",
        wraplength=750  # Limita o tamanho do texto para não ultrapassar a largura
    )
    label.pack(pady=100)

    # Iniciar a exibição dinâmica do texto
    exibir_texto_dinamicamente(label, texto_fase_1_pwd)

    # Manter a nova janela aberta
    nova_janela.mainloop()


# Todo o código existente permanece igual

if __name__ == "__main__":
    criar_segunda_janela()
