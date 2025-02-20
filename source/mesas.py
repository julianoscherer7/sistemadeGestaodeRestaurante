# mesas.py
import tkinter as tk
from tkinter import messagebox
from database import conectar

def listar_mesas():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Mesas")
        mesas = cursor.fetchall()
        conexao.close()
        return mesas
    return []

def tela_mesas():
    janela = tk.Tk()
    janela.title("Mesas")

    mesas = listar_mesas()
    for i, mesa in enumerate(mesas):
        tk.Label(janela, text=f"Mesa {mesa[1]} - Capacidade: {mesa[2]} - Status: {mesa[3]}").grid(row=i, column=0)

    janela.mainloop()

if __name__ == "__main__":
    tela_mesas()