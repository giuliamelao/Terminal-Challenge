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

        self.janela.after(self.intervalo, self.blink)
