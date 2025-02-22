import tkinter as tk
from cadastro import tela_cadastro
from login import tela_login
from principal import tela_principal

class App:
    def __init__(self):
        self.janela_principal = tk.Tk()
        self.janela_principal.withdraw()  # Esconde a janela principal inicialmente
        self.janela_atual = None

    def abrir_tela_login(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        self.janela_atual.protocol("WM_DELETE_WINDOW", self.fechar_programa)  # Fecha o programa ao fechar a janela
        tela_login(self.janela_atual, self.abrir_tela_cadastro, self.abrir_tela_principal)

    def abrir_tela_cadastro(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        self.janela_atual.protocol("WM_DELETE_WINDOW", self.fechar_programa)  # Fecha o programa ao fechar a janela
        tela_cadastro(self.janela_atual, self.abrir_tela_login)

    def abrir_tela_principal(self):
        if self.janela_atual:
            self.janela_atual.destroy()  # Fecha a janela atual
        self.janela_atual = tk.Toplevel(self.janela_principal)
        self.janela_atual.protocol("WM_DELETE_WINDOW", self.fechar_programa)  # Fecha o programa ao fechar a janela
        tela_principal(self.janela_atual, self.abrir_tela_login)

    def fechar_programa(self):
        self.janela_principal.destroy()  # Fecha a janela principal e encerra o programa

    def iniciar(self):
        self.abrir_tela_login()  # Abre a tela de login inicialmente
        self.janela_principal.mainloop()

if __name__ == "__main__":
    app = App()
    app.iniciar()