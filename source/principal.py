import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class TelaPrincipal:
    def __init__(self, parent, callback_login, callback_mesas, callback_pedidos, callback_cardapio, callback_relatorios):
        # Configuração da janela
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#2C3E50")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Fonte moderna para o título
        fonte_titulo = Font(family="Helvetica", size=28, weight="bold")
        fonte_texto = Font(family="Helvetica", size=14)

        # Título
        titulo = tk.Label(self.frame, text="Sistema de Gestão de Restaurante", font=fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=2, pady=40)

        # Botões para outras funcionalidades
        botoes = [
            ("Gerenciar Mesas", callback_mesas),
            ("Gerenciar Pedidos", callback_pedidos),
            ("Gerenciar Cardápio", callback_cardapio),
            ("Gerar Relatórios", callback_relatorios)
        ]

        for i, (texto, comando) in enumerate(botoes):
            botao = tk.Button(
                self.frame,
                text=texto,
                font=fonte_texto,
                bg="#3498DB",
                fg="#FFFFFF",
                activebackground="#2980B9",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=30,
                pady=15,
                command=comando,
                width=20  # Largura fixa para todos os botões
            )
            botao.grid(row=i + 1, column=0, columnspan=2, pady=10, sticky="ew")  # Alinha os botões horizontalmente

        # Botão para voltar ao login
        botao_voltar = tk.Button(
            self.frame,
            text="Voltar para Login",
            font=fonte_texto,
            bg="#E74C3C",
            fg="#FFFFFF",
            activebackground="#C0392B",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            command=callback_login  # Usa o callback para voltar à tela de login
        )
        botao_voltar.grid(row=len(botoes) + 1, column=0, columnspan=2, pady=10, sticky="ew")

    def mostrar(self):
        """Mostra a tela principal."""
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

    def ocultar(self):
        """Oculta a tela principal."""
        self.frame.place_forget()