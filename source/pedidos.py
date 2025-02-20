import tkinter as tk
from tkinter import messagebox
from database import conectar

def criar_pedido(id_mesa):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Pedidos (ID_Mesa) VALUES (%s)", (id_mesa,))
        conexao.commit()
        conexao.close()
        messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")
    else:
        messagebox.showerror("Erro", "Falha ao conectar ao banco de dados.")

def tela_pedidos():
    janela = tk.Tk()
    janela.title("Pedidos")

    tk.Label(janela, text="Número da Mesa:").grid(row=0, column=0)
    entry_mesa = tk.Entry(janela)
    entry_mesa.grid(row=0, column=1)

    tk.Button(janela, text="Criar Pedido", command=lambda: criar_pedido(entry_mesa.get())).grid(row=1, column=1)

    janela.mainloop()

if __name__ == "__main__":
    tela_pedidos()