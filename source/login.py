import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar
from spinner import Spinner

class TelaLogin:
    def __init__(self, parent, callback_cadastro, callback_principal):
        self.parent = parent
        self.callback_cadastro = callback_cadastro
        self.callback_principal = callback_principal
        self.frame = tk.Frame(self.parent, bg="#2C3E50")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Fonte moderna para o título
        fonte_titulo = ("Helvetica", 24, "bold")
        fonte_texto = ("Helvetica", 12)

        # Título
        tk.Label(self.frame, text="Login", font=fonte_titulo, bg="#2C3E50", fg="#ECF0F1").pack(pady=20)

        # Campo de email
        tk.Label(self.frame, text="Email:", bg="#2C3E50", fg="#ECF0F1").pack()
        self.entry_email = tk.Entry(self.frame, font=fonte_texto, width=30)
        self.entry_email.pack(pady=10)

        # Campo de senha
        tk.Label(self.frame, text="Senha:", bg="#2C3E50", fg="#ECF0F1").pack()
        self.entry_senha = tk.Entry(self.frame, font=fonte_texto, width=30, show="*")
        self.entry_senha.pack(pady=10)

        # Botão de login
        tk.Button(
            self.frame,
            text="Entrar",
            font=fonte_texto,
            bg="#3498DB",
            fg="#FFFFFF",
            activebackground="#2980B9",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            command=self.login
        ).pack(pady=20)

        # Botão de cadastro
        tk.Button(
            self.frame,
            text="Cadastrar",
            font=fonte_texto,
            bg="#2ECC71",
            fg="#FFFFFF",
            activebackground="#27AE60",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            command=self.callback_cadastro
        ).pack(pady=10)

        # Label para mensagens de erro
        self.label_erro = tk.Label(self.frame, text="", font=fonte_texto, fg="#E74C3C", bg="#2C3E50")
        self.label_erro.pack()

    def login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        usuario = self.verificar_login(email, senha)
        if usuario:
            self.ocultar()
            self.callback_principal()  # Chama o callback para abrir a tela principal
        else:
            self.label_erro.config(text="Email ou senha incorretos!")

    def verificar_login(self, email, senha):
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Usuarios WHERE Email = %s AND Senha = %s", (email, senha))
            usuario = cursor.fetchone()
            conexao.close()
            return usuario
        return None

    def mostrar(self):
        self.frame.pack()

    def ocultar(self):
        self.frame.pack_forget()

def tela_login(parent, callback_cadastro, callback_principal):
    return TelaLogin(parent, callback_cadastro, callback_principal)