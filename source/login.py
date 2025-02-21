# login.py
import tkinter as tk
from tkinter.font import Font
from database import conectar
from cadastro import tela_cadastro
from principal import tela_principal
from spinner import Spinner  # Importa a classe Spinner

def verificar_login(email, senha):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Email = %s AND Senha = %s", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()
        return usuario
    return None

def mostrar_carregamento(janela, frame):
    # Esconde os elementos do frame
    for widget in frame.winfo_children():
        widget.pack_forget()

    # Mostra o spinner
    spinner = Spinner(janela)

    # Simula um tempo de carregamento
    janela.after(2000, lambda: finalizar_carregamento(janela))

def finalizar_carregamento(janela):
    janela.destroy()  # Fecha a tela de login
    tela_principal()  # Abre a tela principal

def tela_login():
    def login():
        email = entry_email.get()
        senha = entry_senha.get()
        usuario = verificar_login(email, senha)
        if usuario:
            mostrar_carregamento(janela, frame)  # Mostra o spinner
        else:
            label_erro.config(text="Email ou senha incorretos!", fg="#E74C3C")

    # Configuração da janela
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("800x600")  # Resolução maior
    janela.configure(bg="#2C3E50")  # Fundo azul escuro moderno

    # Frame principal
    frame = tk.Frame(janela, bg="#2C3E50")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

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
        bg="#3498DB",  # Azul mais claro
        fg="#FFFFFF",  # Texto branco
        activebackground="#2980B9",  # Azul mais escuro ao clicar
        activeforeground="#FFFFFF",
        relief="flat",  # Remove borda padrão
        bd=0,  # Remove borda
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
        bg="#2ECC71",  # Verde
        fg="#FFFFFF",  # Texto branco
        activebackground="#27AE60",  # Verde mais escuro ao clicar
        activeforeground="#FFFFFF",
        relief="flat",  # Remove borda padrão
        bd=0,  # Remove borda
        padx=20,
        pady=10,
        command=tela_cadastro  # Abre a tela de cadastro
    )
    botao_cadastro.pack(pady=10)

    # Label para mensagens de erro
    label_erro = tk.Label(frame, text="", font=fonte_texto, fg="#E74C3C", bg="#2C3E50")
    label_erro.pack()

    janela.mainloop()

if __name__ == "__main__":
    tela_login()