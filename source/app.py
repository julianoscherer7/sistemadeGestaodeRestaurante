import tkinter as tk
from tkinter import ttk
from login import tela_login  # Importa a função tela_login
from principal import TelaPrincipal  # Importa a classe TelaPrincipal
from mesas import tela_mesas
from pedidos import tela_pedidos
from cardapio import tela_cardapio
from relatorios import tela_relatorios
from cadastro import tela_cadastro  # Importa a função tela_cadastro

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x768")
        self.root.title("Sistema de Gestão de Restaurante")
        self.root.configure(bg="#2C3E50")

        # Inicializa apenas a tela de login
        self.tela_login = tela_login(self.root, self.abrir_cadastro, self.abrir_principal)  # Passa os callbacks corretos

        # Inicia com a tela de login
        self.tela_login.mostrar()

        # Inicializa as outras telas como None (elas serão criadas apenas quando necessário)
        self.tela_principal = None
        self.tela_mesas = None
        self.tela_pedidos = None
        self.tela_cardapio = None
        self.tela_relatorios = None

    def iniciar(self):
        self.root.mainloop()

    def abrir_principal(self):
        # Cria a tela principal apenas se ainda não foi criada
        if self.tela_principal is None:
            self.tela_principal = TelaPrincipal(self.root, self.voltar_login, self.abrir_mesas, self.abrir_pedidos, self.abrir_cardapio, self.abrir_relatorios)
        
        self.tela_login.ocultar()
        self.tela_principal.mostrar()

    def voltar_login(self):
        if self.tela_principal is not None:
            self.tela_principal.ocultar()
        self.tela_login.mostrar()

    def abrir_cadastro(self):
        # Fecha a tela de login temporariamente
        self.tela_login.ocultar()
        
        # Abre a tela de cadastro
        tela_cadastro(self.root, self.voltar_login)

    def abrir_mesas(self):
        # Verifica se a tela principal está criada
        if self.tela_principal is not None:
            self.tela_principal.ocultar()
        
        # Cria a tela de mesas apenas se ainda não foi criada
        if self.tela_mesas is None:
            self.tela_mesas = tela_mesas(self.root, self.voltar_principal)
        
        self.tela_mesas.mostrar()

    def abrir_pedidos(self):
        # Verifica se a tela principal está criada
        if self.tela_principal is not None:
            self.tela_principal.ocultar()
        
        # Cria a tela de pedidos apenas se ainda não foi criada
        if self.tela_pedidos is None:
            self.tela_pedidos = tela_pedidos(self.root, self.voltar_principal)
        
        self.tela_pedidos.mostrar()

    def abrir_cardapio(self):
        # Verifica se a tela principal está criada
        if self.tela_principal is not None:
            self.tela_principal.ocultar()
        
        # Cria a tela de cardápio apenas se ainda não foi criada
        if self.tela_cardapio is None:
            self.tela_cardapio = tela_cardapio(self.root, self.voltar_principal)
        
        self.tela_cardapio.mostrar()

    def abrir_relatorios(self):
        # Verifica se a tela principal está criada
        if self.tela_principal is not None:
            self.tela_principal.ocultar()
        
        # Cria a tela de relatórios apenas se ainda não foi criada
        if self.tela_relatorios is None:
            self.tela_relatorios = tela_relatorios(self.root, self.voltar_principal)
        
        self.tela_relatorios.mostrar()

    def voltar_principal(self):
        # Função para voltar à tela principal
        if self.tela_mesas is not None:
            self.tela_mesas.ocultar()
        if self.tela_pedidos is not None:
            self.tela_pedidos.ocultar()
        if self.tela_cardapio is not None:
            self.tela_cardapio.ocultar()
        if self.tela_relatorios is not None:
            self.tela_relatorios.ocultar()
        
        if self.tela_principal is not None:
            self.tela_principal.mostrar()

if __name__ == "__main__":
    app = App()
    app.iniciar()