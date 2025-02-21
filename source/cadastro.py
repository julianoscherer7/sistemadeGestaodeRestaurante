# cadastro.py
import tkinter as tk
from tkinter.font import Font
from database import conectar
from spinner import Spinner  # Importa a classe Spinner

def cadastrar_usuario(nome, email, senha):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Usuarios (Nome, Email, Senha) VALUES (%s, %s, %s)", (nome, email, senha))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            return False
        finally:
            conexao.close()
    else:
        print("Falha ao conectar ao banco de dados.")
        return False

def mostrar_carregamento(janela, frame):
    # Esconde os elementos do frame
    for widget in frame.winfo_children():
        widget.pack_forget()

    # Mostra o spinner
    spinner = Spinner(janela)

    # Simula um tempo de carregamento
    janela.after(2000, lambda: finalizar_carregamento(janela))

def finalizar_carregamento(janela):
    janela.destroy()  # Fecha a tela de cadastro

def tela_cadastro():
    def realizar_cadastro():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if nome and email and senha:
            if cadastrar_usuario(nome, email, senha):
                mostrar_carregamento(janela, frame)  # Mostra o spinner
        else:
            label_erro.config(text="Preencha todos os campos!", fg="#E74C3C")

    # Configuração da janela
    janela = tk.Tk()
    janela.title("Cadastro")
    janela.geometry("400x300")  # Tamanho maior
    janela.configure(bg="#2C3E50")  # Fundo azul escuro moderno

    # Frame principal
    frame = tk.Frame(janela, bg="#2C3E50")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

    # Fonte moderna
    fonte_texto = Font(family="Helvetica", size=12)

    # Título
    titulo = tk.Label(frame, text="Cadastro", font=("Helvetica", 18, "bold"), fg="#ECF0F1", bg="#2C3E50")
    titulo.pack(pady=10)

    # Campo de nome
    label_nome = tk.Label(frame, text="Nome:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_nome.pack()
    entry_nome = tk.Entry(frame, font=fonte_texto, width=25)
    entry_nome.pack(pady=5)

    # Campo de email
    label_email = tk.Label(frame, text="Email:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_email.pack()
    entry_email = tk.Entry(frame, font=fonte_texto, width=25)
    entry_email.pack(pady=5)

    # Campo de senha
    label_senha = tk.Label(frame, text="Senha:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_senha.pack()
    entry_senha = tk.Entry(frame, font=fonte_texto, width=25, show="*")
    entry_senha.pack(pady=5)

    # Botão de cadastro
    botao_cadastro = tk.Button(
        frame,
        text="Cadastrar",
        font=fonte_texto,
        bg="#3498DB",  # Azul mais claro
        fg="#FFFFFF",  # Texto branco
        activebackground="#2980B9",  # Azul mais escuro ao clicar
        activeforeground="#FFFFFF",
        relief="flat",  # Remove borda padrão
        bd=0,  # Remove borda
        padx=20,
        pady=10,
        command=realizar_cadastro
    )
    botao_cadastro.pack(pady=20)

    # Label para mensagens de erro
    label_erro = tk.Label(frame, text="", font=fonte_texto, fg="#E74C3C", bg="#2C3E50")
    label_erro.pack()

    janela.mainloop()

if __name__ == "__main__":
    tela_cadastro()