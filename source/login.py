import tkinter as tk
from tkinter.font import Font
from database import conectar
from spinner import Spinner

def verificar_login(email, senha):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Email = %s AND Senha = %s", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()
        return usuario
    return None

def mostrar_carregamento(janela, frame, callback):
    # Esconde os elementos do frame
    for widget in frame.winfo_children():
        widget.pack_forget()

    # Mostra o spinner
    spinner = Spinner(janela)

    # Simula um tempo de carregamento
    janela.after(2000, lambda: finalizar_carregamento(janela, callback))

def finalizar_carregamento(janela, callback):
    janela.destroy()  # Fecha a tela de login
    callback()  # Chama o callback para abrir a próxima tela

def tela_login(parent, callback_cadastro, callback_principal):
    def login():
        email = entry_email.get()
        senha = entry_senha.get()
        usuario = verificar_login(email, senha)
        if usuario:
            mostrar_carregamento(janela, frame, callback_principal)  # Passa o callback para a tela principal
        else:
            label_erro.config(text="Email ou senha incorretos!", fg="#E74C3C")

    # Configuração da janela
    janela = parent
    janela.title("Login")
    janela.geometry("1280x720")
    janela.configure(bg="#2C3E50")

    # Frame principal
    frame = tk.Frame(janela, bg="#2C3E50")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Fonte moderna para o título
    fonte_titulo = Font(family="Helvetica", size=24, weight="bold")
    fonte_texto = Font(family="Helvetica", size=12)

    # Título
    titulo = tk.Label(frame, text="Login", font=fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
    titulo.pack(pady=20)

    # Campo de email
    label_email = tk.Label(frame, text="Email:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_email.pack()
    entry_email = tk.Entry(frame, font=fonte_texto, width=30)
    entry_email.pack(pady=10)

    # Campo de senha
    label_senha = tk.Label(frame, text="Senha:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_senha.pack()
    entry_senha = tk.Entry(frame, font=fonte_texto, width=30, show="*")
    entry_senha.pack(pady=10)

    # Botão de login
    botao_login = tk.Button(
        frame,
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
        command=login
    )
    botao_login.pack(pady=20)

    # Botão de cadastro
    botao_cadastro = tk.Button(
        frame,
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
        command=callback_cadastro  # Usa o callback para abrir a tela de cadastro
    )
    botao_cadastro.pack(pady=10)

    # Label para mensagens de erro
    label_erro = tk.Label(frame, text="", font=fonte_texto, fg="#E74C3C", bg="#2C3E50")
    label_erro.pack()