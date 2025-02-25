import tkinter as tk
from tkinter import ttk
from login import tela_login  # Importa a função tela_login
from principal import tela_principal
from mesas import tela_mesas
from pedidos import tela_pedidos
from cardapio import tela_cardapio
from relatorios import tela_relatorios

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x768")
        self.root.title("Sistema de Gestão de Restaurante")
        self.root.configure(bg="#2C3E50")

        # Inicializa as telas
        self.tela_login = tela_login(self.root, self.abrir_cadastro, self.abrir_principal)  # Passa os callbacks corretos
        self.tela_principal = tela_principal(self.root, self.voltar_login, self.abrir_mesas, self.abrir_pedidos, self.abrir_cardapio, self.abrir_relatorios)
        self.tela_mesas = tela_mesas(self.root, self.voltar_principal)  # Passa o callback para voltar à tela principal
        self.tela_pedidos = tela_pedidos(self.root, self.voltar_principal)  # Passa o callback para voltar à tela principal
        self.tela_cardapio = tela_cardapio(self.root, self.voltar_principal)  # Passa o callback para voltar à tela principal
        self.tela_relatorios = tela_relatorios(self.root, self.voltar_principal)  # Passa o callback para voltar à tela principal

        # Inicia com a tela de login
        self.tela_login.mostrar()

    def iniciar(self):
        self.root.mainloop()

    def abrir_principal(self):
        self.tela_login.ocultar()
        self.tela_principal.mostrar()

    def voltar_login(self):
        self.tela_principal.ocultar()
        self.tela_login.mostrar()

    def voltar_principal(self):
        # Função para voltar à tela principal
        self.tela_mesas.ocultar()
        self.tela_pedidos.ocultar()
        self.tela_cardapio.ocultar()
        self.tela_relatorios.ocultar()
        self.tela_principal.mostrar()

    def abrir_cadastro(self):
        # Função para abrir a tela de cadastro (se necessário)
        print("Abrir tela de cadastro")

    def abrir_mesas(self):
        self.tela_principal.ocultar()
        self.tela_mesas.mostrar()

    def abrir_pedidos(self):
        self.tela_principal.ocultar()
        self.tela_pedidos.mostrar()

    def abrir_cardapio(self):
        self.tela_principal.ocultar()
        self.tela_cardapio.mostrar()

    def abrir_relatorios(self):
        self.tela_principal.ocultar()
        self.tela_relatorios.mostrar()

if __name__ == "__main__":
    app = App()
    app.iniciar()