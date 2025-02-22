import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class Spinner:
    def __init__(self, janela, gif_path="source/spinner.gif", frame_interval=100):
        self.janela = janela
        self.frame_atual = 0
        self.frames = []  # Lista para armazenar as referências das imagens
        self.frame_interval = frame_interval  # Intervalo entre os frames em milissegundos

        try:
            # Tenta carregar o GIF do spinner
            self.spinner_gif = Image.open(gif_path)
            # Armazena os frames do GIF em uma lista
            self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.spinner_gif)]
        except Exception as e:  # Captura qualquer exceção
            print(f"Erro ao carregar o spinner: {e}")  # Imprime o erro completo

        # Cria um label para exibir o spinner
        self.label_spinner = tk.Label(janela, bg="#2C3E50")
        self.label_spinner.place(relx=0.5, rely=0.5, anchor="center")

        # Inicia a animação se o GIF foi carregado corretamente
        if self.frames:
            self.animar_spinner()
        else:
            # Exibe uma mensagem de erro se o GIF não foi encontrado
            self.label_spinner.config(text="Erro: spinner.gif não encontrado!", fg="#E74C3C")

    def animar_spinner(self):
        # Atualiza o frame do spinner
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.label_spinner.config(image=self.frames[self.frame_atual])

        # Agenda a próxima atualização
        self.janela.after(self.frame_interval, self.animar_spinner)  # Usa o intervalo personalizado