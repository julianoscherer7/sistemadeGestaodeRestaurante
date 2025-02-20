# login.py
import tkinter as tk
from tkinter import messagebox
from database import conectar
from principal import tela_principal  # Importe a tela principal

def verificar_login(email, senha):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Email = %s AND Senha = %s", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()
        return usuario
    return None

def tela_login():
    def login():
        email = entry_email.get()
        senha = entry_senha.get()
        usuario = verificar_login(email, senha)
        if usuario:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela.destroy()  # Fecha a janela de login
            tela_principal()  # Abre a tela principal
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")

    janela = tk.Tk()
    janela.title("Login")

    tk.Label(janela, text="Email:").grid(row=0, column=0)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=0, column=1)

    tk.Label(janela, text="Senha:").grid(row=1, column=0)
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.grid(row=1, column=1)

    tk.Button(janela, text="Entrar", command=login).grid(row=2, column=1)

    janela.mainloop()

if __name__ == "__main__":
    tela_login()