import tkinter as tk
from login import tela_login
from cadastro import tela_cadastro  # Importação adicionada
from principal import tela_principal
from mesas import tela_mesas

class App:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.withdraw()  # Esconde a janela principal inicialmente
        self.janela_atual = None

    def abrir_tela_login(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        tela_login(self.janela_atual, self.abrir_tela_cadastro, self.abrir_tela_principal)

    def abrir_tela_cadastro(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        tela_cadastro(self.janela_atual, self.abrir_tela_login)

    def abrir_tela_principal(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        tela_principal(self.janela_atual, self.abrir_tela_login, self.abrir_tela_mesas)

    def abrir_tela_mesas(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        tela_mesas(self.janela_atual, self.abrir_tela_principal)

    def iniciar(self):
        self.abrir_tela_login()  # Abre a tela de login inicialmente
        self.janela_principal.mainloop()

if __name__ == "__main__":
    app = App()
    app.iniciar()