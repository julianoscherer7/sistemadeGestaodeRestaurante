import tkinter as tk
from tkinter import messagebox
from database import conectar

def listar_itens():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Itens")
        itens = cursor.fetchall()
        conexao.close()
        return itens
    return []

def tela_cardapio():
    janela = tk.Tk()
    janela.title("Cardápio")

    itens = listar_itens()
    for i, item in enumerate(itens):
        tk.Label(janela, text=f"{item[1]} - R${item[3]}").grid(row=i, column=0)

    janela.mainloop()

if __name__ == "__main__":
    tela_cardapio()